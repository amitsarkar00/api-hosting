from .models import Meeting
from .serializers import MeetingSerializer

from rest_framework import viewsets, permissions
from users.permissions import IsAdmin

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meetings to be viewed or edited.
    """
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]