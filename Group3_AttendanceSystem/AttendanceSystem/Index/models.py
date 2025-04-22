from django.db import models
# Create your models here.

class User(models.Model):
    type_user = (('S', 'Student'), ('T', 'Teacher'), (''))
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=1, choices=type_user)
