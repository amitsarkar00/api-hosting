from rest_framework.exceptions import ValidationError
from companies.models import Admin, Company, Hr
from users.models import User, Candidate
from rest_framework.authtoken.models import Token
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate
from django.db.models import F
from django.shortcuts import get_object_or_404
from asgiref.sync import sync_to_async

from rest_framework import views, response, viewsets, authentication, permissions
from rest_framework.decorators import action

from .serializers import AdminUserSerializer, CandidateUserSerializer, HrUserSerializer, UserSerializer, CandidateSerializer
from .helper import generateOTP, get_token_by_user, verifyOTP, email_verification_send, filter_dict
from users.permissions import IsCandidate, IsAdmin, IsHr, allow_login

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'retrive':
            permission_classes = [IsAdmin | IsHr]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        if(user.role == User.Roles.USER):
            serializer = CandidateUserSerializer(user)
        elif(user.role == User.Roles.HR):
            serializer = HrUserSerializer(user)
        elif(user.role == User.Roles.ADMIN):
            serializer = AdminUserSerializer(user)
        else:
            serializer = UserSerializer(user)
        return response.Response(serializer.data)

    # @action(detail=False, methods=['post'], permission_classes=[IsAdmin])
    # def registerHr(self, *args, **kwargs):
    #     return super(viewsets.ModelViewSet, self).create(*args, **kwargs)

class CreateUserView(views.APIView):
    """
    Creating different users with different roles
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, req, format=None):
        body = req.data
        role = req.query_params.get('role')
        user = None
        if not role :
            return response.Response({"error" : "role not found in query params"}, status=404)
        if role == 'candidate':
            user_serializer = UserSerializer(data=body)
            if user_serializer.is_valid() :
                user = user_serializer.save()
                Candidate.objects.create(user=user)
        elif role == 'hr' or role == 'admin':
            company_id = body.pop('company_id', None)
            if not company_id:
                return response.Response({"error" : "company_id is required"}, status=404)
            company = Company.objects.filter(id=company_id)
            if not company.exists():
                return response.Response({"error" : "company_id not valid\nPlease enter correct company_id or create a company first"}, status=404)
            company = company.get()
            req_user = None
            verified = False

            try:
                req_user = req.user
                if req_user and req_user.role == User.Roles.ADMIN and hasattr(req_user, 'admin') and req_user.admin.company.id == company_id:
                    verified = True
            except:
                req_user = None
            
            if role == 'hr':
                user_serializer = UserSerializer(data=body)
                if user_serializer.is_valid() :
                    user = user_serializer.save()
                    user.role = User.Roles.HR
                    user.save()
                    Hr.objects.create(user=user, company=company, created_by=req_user, allow_login=verified)
            else :
                user_serializer = UserSerializer(data=body)
                if user_serializer.is_valid() :
                    user = user_serializer.save()
                    user.role = User.Roles.ADMIN
                    user.save()
                    Admin.objects.create(user=user, company=company, created_by=req_user, allow_login=verified)
        if not user:
            return response.Response({"error" : "Invalid Data"}, status=404)
        return response.Response({"message" : f"User created with role {role} and id {user.id}"}, status=201)


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoggedInUser(views.APIView):
    """
    User details of current user
    """

    authentication_classes = [authentication.TokenAuthentication , authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, req, format=None):
        """
        Get user details of current user
        """
        user = req.user
        if(user.role == User.Roles.USER):
            serializer = CandidateUserSerializer(user)
        elif(user.role == User.Roles.HR):
            serializer = HrUserSerializer(user)
        elif(user.role == User.Roles.ADMIN):
            serializer = AdminUserSerializer(user)
        else:
            serializer = UserSerializer(user)
        return response.Response(serializer.data)

class Login(views.APIView):
    """
    Authenticate user
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, req, format=None):
        body = req.data
        try:
            email = body['email']
        except:
            return response.Response({"error" : "Email required"}, status=404)
        try:
            password = body['password']
        except:
            return response.Response({"error" : "Password required"}, status=404)

        user = authenticate(email=email, password=password)

        if(not user):
            return response.Response({
                "error" : "Invalid credentials"
            }, status=404)

        if user.role != User.Roles.USER and not (allow_login(user, 'hr') or allow_login(user, 'admin')):
            return response.Response({"error" : "Login access not provided by Admin"}, status=404)

        return response.Response(get_token_by_user(user))


class VerifyOTP(views.APIView):
    """
    Email/ Phone Number verification through OTP API
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, req, format=None):
        """
        Generates OTP for email/phone_number verification
        """

        field = req.query_params.get('field','')
        digits = int(req.query_params.get('digits', 6))
        valid_for = int(req.query_params.get('valid_for', 120))
        data = req.query_params.get('data')
        otp = generateOTP(data, field, digits, valid_for)

        if(field == 'email'):

            email_verification_send(data, otp)
            return response.Response({
                "valid_for" : valid_for,
                "digits" : digits
            })
        
        elif(field == 'phone_number'):

            return response.Response({
                "otp" : otp,
                "valid_for" : valid_for,
                "digits" : digits
            })

        return response.Response({
            "error" : "Field not found."
        }, 404)

    def post(self, req, format=None):
        """
        Verifies OTP for email/phone_number verification
        """

        field = req.query_params.get('field')
        otp = req.data.get('otp')
        data = req.data.get('data','')

        if(field == 'email'):
            if verifyOTP(data, field, otp):
                #otp login
                user = User.objects.filter(email=data)
                if user.exists():
                    return response.Response(get_token_by_user(user.get()))
                else:
                    return response.Response()
        
        elif(field == 'phone_number'):
            if verifyOTP(data, field, otp):
                return response.Response()
        else:
            return response.Response({
                "error" : "Field not found."
            }, 404)

        return response.Response({
            "error" : "OTP not valid or OTP has expired."
        }, 404)

