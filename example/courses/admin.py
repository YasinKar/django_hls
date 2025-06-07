from django.contrib import admin
from .models import Course, CourseSession

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseSession)