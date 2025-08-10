from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import *


admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
