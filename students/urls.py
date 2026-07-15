from django.urls import path
from .views import StudentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentView)

urlpatterns = router.urls