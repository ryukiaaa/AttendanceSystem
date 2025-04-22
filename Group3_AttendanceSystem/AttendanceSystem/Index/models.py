from django.db import models
from django.contrib.auth.models import User

# User profile extension for role management
class UserProfile(models.Model):
    ROLE_CHOICES = (('student', 'Student'), ('teacher', 'Teacher'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class StudentProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()

class TeacherProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department_id = models.CharField(max_length=20)
    courses = models.CharField(max_length=200)

# If you have other models, keep them below
