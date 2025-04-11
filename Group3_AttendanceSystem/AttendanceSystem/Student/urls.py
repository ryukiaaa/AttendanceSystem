# Student URLs
from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', permission_required('Student.view_student', raise_exception=True)(views.StudentDashboard.as_view()), name='dashboard')
]
