from rest_framework import routers
from .views import ResumeViewSet

router = routers.DefaultRouter()
router.register(r'resume', ResumeViewSet)

urlpatterns = router.urls