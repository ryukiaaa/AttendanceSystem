from django.db import models
from Index import models

# Create your models here.

class Teacher(User):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher_id}-{self.last_name}"