from rest_framework import routers
from .views import AdminViewSet, CompanyViewSet, HrViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'hrs', HrViewSet)

urlpatterns = router.urls