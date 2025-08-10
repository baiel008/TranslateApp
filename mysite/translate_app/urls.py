from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'teacher', TeacherViewSet, basename='teacher_list')
router.register(r'student', StudentViewSet, basename='student_list')

urlpatterns = [
    path('', include(router.urls)),
]