from .models import File
from .serializers import FileSerializer

from rest_framework import viewsets, permissions
from users.permissions import IsAdmin

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Files to be viewed or edited.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]