# Index URLs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('register/student/', views.RegisterStudent.as_view(), name='registerstudent'),
    path('register/teacher/', views.RegisterTeacher.as_view(), name='registerteacher'),
]
