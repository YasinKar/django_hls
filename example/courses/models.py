from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django_hls.models import DjangoHLSMedia


class Course(models.Model):
    title = models.CharField(max_length=250)
    rate = models.IntegerField(
        default=1,
        verbose_name='Stars',
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# this will add media, hls_file, key_file fields to model
class CourseSession(DjangoHLSMedia):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_sessions')
    title = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.course.title} - {self.title}'