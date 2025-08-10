from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'teacher', TeacherViewSet, basename='teacher_list')
router.register(r'student', StudentViewSet, basename='student_list')

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/create/<int:pk>/', CourseCreateAPIView.as_view(), name='course_create'),
    path('lesson/create/<int:pk>/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('assignment/create/<int:pk>/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('assignment/create/<int:pk>/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('exam/create/<int:pk>/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('certificate/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate_detail'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
]