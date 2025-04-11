# Index URLs
from django.urls import path
from . import views

urlpatterns = [
    path('register/role/', views.register_role_view, name='registerrole'),
    path('register/student/', views.register_student_view, name='registerstudent'),
    path('register/teacher/', views.register_teacher_view, name='registerteacher'),
    path('login/role/', views.login_role_view, name='loginrole'),
    path('login/student/', views.login_student_view, name='loginstudent'),
    path('login/teacher/', views.login_teacher_view, name='loginteacher'),
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register')
]
