from rest_framework import routers
from .views import UserViewSet, CandidateViewSet
from django.urls import path, include
from .views import VerifyOTP, LoggedInUser, Login, CreateUserView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'candidates', CandidateViewSet)

urlpatterns = [
    # path('email/<uuid:token>/', verify_email, name='verify_email'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('verify/otp/', VerifyOTP.as_view(), name='verify_otp'),
    path('user/', LoggedInUser.as_view(), name='logged_in_user'),
    path('login/', Login.as_view(), name='customized login'),
    path('api/v1/register/', CreateUserView.as_view(), name='multiple role user registration'),
]
