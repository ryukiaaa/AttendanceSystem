from django.db import models
from Student import models
from Teacher import models

# Create your models here.

class User(models.Model):
    type_user = (('S', 'Student'), ('T', 'Teacher'))
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=1, choice=type_user)


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