from .models import Resume
from .serializers import ResumeSerializer

from rest_framework import viewsets, permissions

# Create your views here.
class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Resumes to be viewed or edited.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]