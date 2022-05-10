from rest_framework import routers
from .views import FileViewSet

router = routers.DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = router.urls