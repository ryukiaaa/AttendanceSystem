from django.urls import path
from .views import Home, Login, Register, RegisterTeacher, RegisterStudent

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('registerteacher', RegisterTeacher.as_view(), name='registerteacher'),
    path('registerstudent', RegisterStudent.as_view(), name='registerstudent'),
]