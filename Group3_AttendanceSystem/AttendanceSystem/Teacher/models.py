from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(User):
    department = models.CharField(max_length=20)

    class Meta:
        db_table = 'tbl_teachers'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    # Hash the password in the database upon creation of a new student
    def save(self):
        self.set_password(self.password)
        super().save()

    # Changed displayed model name in admin site
    def __str__(self):
        first_name = super(User, self).first_name
        last_name = super(User, self).last_name

        return first_name + ' ' + last_name


class Class(models.Model):
    class_id = models.BigAutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=20, unique=True)
    join_code = models.CharField(max_length=20, unique=True)
    building_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    schedule1_day = models.CharField(max_length=20)
    schedule1_start = models.TimeField()
    schedule1_end = models.TimeField()
    schedule2_day = models.CharField(max_length=20)
    schedule2_start = models.TimeField()
    schedule2_end = models.TimeField()

    # ONE-TO-MANY RELATIONSHIP: A teacher handles many classes
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='handles')

    # MANY-TO-MANY RELATIONSHIP: A class has many students and students can join many classes
    students = models.ManyToManyField('Student.Student', through='Student.Attendance', related_name='joins')

    # Change displayed model name in admin site
    class Meta:
        db_table = 'tbl_classes'
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    # Show class code in the admin site
    def __str__(self):
        return self.class_code
