from django.db import models
from django.contrib.auth.models import User

# Importing model 'Student' causes an ImportError:
# "cannot import name 'Student' from partially initialized module 'Student.models'
# (most likely due to a circular import)"
# RESOLVED: On line 42, used 'Appname.Modelname' as parameter instead
# from Student.models import Student

# Create your models here.
class Teacher(User):
    department = models.CharField(max_length=100)

    # Makes sure the password is hashed in the database when a new teacher is created
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    # Show firstname and lastname in admin site
    def __str__(self):
        # Get inherited fields
        first_name = super(User, self).first_name
        last_name = super(User, self).last_name

        return first_name + ' ' + last_name


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=20, unique=True)
    join_code = models.CharField(max_length=50, unique=True) # Could be converted to a QR code (maybe?)
    building_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    schedule1 = models.CharField(max_length=100)
    schedule2 = models.CharField(max_length=100)

    # ONE-TO-MANY RELATIONSHIP: A teacher handles many classes
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='handles')

    # MANY-TO-MANY RELATIONSHIP: A class has many students and students join many classes
    students = models.ManyToManyField('Student.Student', through='Student.Attendance', related_name='joins')

    # Show class code in the admin site
    def __str__(self):
        return self.class_code
