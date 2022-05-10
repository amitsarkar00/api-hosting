from .models import Company, Hr, Admin
from .serializers import CompanySerializer, HrSerializer, AdminSerializer

from rest_framework import viewsets, permissions
from users.permissions import IsAdmin

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Admins to be viewed or edited.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class HrViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hrs to be viewed or edited.
    """
    queryset = Hr.objects.all()
    serializer_class = HrSerializer
    permission_classes = [permissions.IsAuthenticated]