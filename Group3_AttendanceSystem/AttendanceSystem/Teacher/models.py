from datetime import time

from django.db import models
from Index.models import User

# Create your models here.

class Teacher(User):
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}-{self.lastname}"


class Class(models.Model):
    class_id = models.CharField(max_length=20, primary_key=True)
    class_name = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    schedule = models.DateTimeField()
    schedule_end = models.TimeField(default=time(0, 0))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')


    def __str__(self):
        return self.class_id