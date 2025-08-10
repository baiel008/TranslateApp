from .models import *
from rest_framework import serializers


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', ]


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', ]



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', ]