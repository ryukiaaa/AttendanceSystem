from django.db import models
from Index.models import User

# Create your models here.

class Teacher(User):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher_id}-{self.last_name}"


class Class(models.Model):
    class_id = models.CharField(max_length=20, primary_key=True)
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=20, unique=True)
    building_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    schedule = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.class_code