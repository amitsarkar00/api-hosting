from rest_framework import routers
from .views import MeetingViewSet

router = routers.DefaultRouter()
router.register(r'meetings', MeetingViewSet)

urlpatterns = router.urls