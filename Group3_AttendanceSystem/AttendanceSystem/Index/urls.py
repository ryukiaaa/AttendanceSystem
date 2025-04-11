# Authentication URLs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'), #localhost:8000
    path('login/', views.Login.as_view(), name='login'), #localhost:8000/login
    path('register/', views.Register.as_view(), name='register'), #localhost:8000/register
    path('register/student/', views.RegisterStudent.as_view(), name='registerstudent'), #localhost:8000/register/student
    path('register/teacher/', views.RegisterTeacher.as_view(), name='registerteacher'), #localhost:8000/register/teacher
]
