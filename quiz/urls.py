from django.urls import path
from rest_framework import routers
from .views import QuizViewSet #, QuizListView

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)
# router.register(r'quizlist', QuizListView)

urlpatterns = router.urls
