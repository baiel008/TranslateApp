from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

from mysite.mysite.settings import USE_TZ

ROLE_CHOICES = (
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
)


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255, verbose_name='Емайл')
    passwrod = models.CharField(max_length=255, verbose_name='Пароль')

    def __str__(self):
        return f'{self.username}, {self.full_name}'




class Teacher(UserProfile):
    bio = models.TextField()
    subjects = models.TextField()
    experience = models.PositiveSmallIntegerField(validators=[MaxValueValidator(40)])
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='Teacher')

    def __str__(self):
        return f'{self.role}'


class Student(models.Model):
    class Student(models.Model):
        user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
        role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='teacher')

        def __str__(self):
            return f'{self.user}, {self.role}'



