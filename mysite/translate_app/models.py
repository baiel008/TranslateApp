from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField


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


class Category(models.Model):
    category = models.CharField(max_length=32)

    def str(self):
        return f'{self.category}'


class Video(models.Model):
    video = models.FileField(upload_to='videos/')




class Course(models.Model):
    course_name  = models.CharField(max_length=128)
    description  = models.TextField()
    category  = models.ForeignKey(Category, on_delete=models.CASCADE,
                                  related_name='category_name')
    LEVEL_CHOICES  = [
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый')
    ]
    level  = models.CharField(max_length=32, choices=LEVEL_CHOICES, default='начальный')
    price  = models.PositiveSmallIntegerField()
    created_by  = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Lesson(models.Model):
    title  = models.CharField(max_length=128)
    video_url  = models.URLField()
    content  = models.TextField()


class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    LEVEL_CHOICES = [
        ('лёгкий', 'лёгкий'),
        ('средний', 'средний'),
        ('сложный', 'сложный')
    ]
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, default='лёгкий')
    due_date = models.DateTimeField()
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    submitted_by = models.TextField()


class Exam(models.Model):
    title = models.CharField(max_length=128)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.CharField(max_length=200)
    passing_score = models.PositiveSmallIntegerField()



class Certificate(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.CharField(max_length=255)


class Review(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                        null=True, blank=True)
    comment = models.TextField()

