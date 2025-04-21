# Student URLs

from django.contrib.auth.decorators import permission_required
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', permission_required('Student.view_student', raise_exception=True)(views.StudentDashboard.as_view()), name='dashboard'),
    path('dashboard/logout/', views.Logout.as_view(), name='logout'),
]
