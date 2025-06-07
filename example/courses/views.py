from django.views.generic import DetailView, ListView

from .models import Course, CourseSession


class SessionView(DetailView):
    model = CourseSession
    template_name = 'courses/session.html'
    context_object_name = 'session'
    
class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'