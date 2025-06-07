from django.urls import path

from .views import SessionView, CourseListView

urlpatterns = [
    path('<pk>', SessionView.as_view(), name='session'),
    path('', CourseListView.as_view(), name='index'),
]
