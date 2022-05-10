from .models import Interview
from .serializers import InterviewSerializer

from rest_framework import viewsets, permissions
from users.permissions import IsAdmin, IsHr

# Create your views here.
class InterviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Interviews to be viewed or edited.
    """
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]