from users.models import User
from .models import Job
from .serializers import JobSerializer

from rest_framework import viewsets, permissions
from users.permissions import IsAdmin, IsCandidate, IsHr

# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed or edited.
    """
    queryset = Job.objects.select_related('posted_by').all()
    serializer_class = JobSerializer
    permission_classes = [IsCandidate | IsHr | IsAdmin]

    def get_queryset(self):
        queryset = Job.objects.select_related('posted_by').all()
        user = self.request.user
        if(user.role == User.Roles.USER):
            return queryset
        elif(user.role == User.Roles.ADMIN):
            hr_ids = user.admin.company.hr_set.all().values_list('user__id', flat=True)
            admin_ids = user.admin.company.admin_set.all().values_list('user__id', flat=True)
            user_ids = hr_ids.union(admin_ids)
            return queryset.filter(posted_by__in=user_ids)
        else:
            return queryset.filter(posted_by=user)