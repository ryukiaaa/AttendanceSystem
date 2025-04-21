# Teacher URLs

from django.contrib.auth.decorators import permission_required
from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', permission_required('Teacher.view_teacher', raise_exception=True)(views.TeacherDashboard.as_view()), name='dashboard'),
    path('createclass/', permission_required('Teacher.view_teacher', raise_exception=True)(views.CreateClass.as_view()), name='createclass'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
