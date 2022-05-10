from rest_framework import routers
from .views import InterviewViewSet

router = routers.DefaultRouter()
router.register(r'interviews', InterviewViewSet)

urlpatterns = router.urls