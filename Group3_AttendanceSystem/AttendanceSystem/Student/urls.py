# Student URLs
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', views.StudentDashboard.as_view(), name='dashboard'),
    path('newdashboard/', views.NewStudentDashboard.as_view(), name='newdashboard')
]
