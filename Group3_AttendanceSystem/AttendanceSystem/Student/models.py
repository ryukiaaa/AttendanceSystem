from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(User):
    course = models.CharField(max_length=20)
    year = models.IntegerField()

    class Meta:
        db_table = 'tbl_students'
        verbose_name = 'student'
        verbose_name_plural = 'students'

    # Hash the password in the table upon creation of a new student
    def save(self):
        self.set_password(self.password)
        super().save()

    # Changed displayed model name in admin site
    def __str__(self):
        first_name = super(User, self).first_name
        last_name = super(User, self).last_name

        return first_name + ' ' + last_name


class Attendance(models.Model):
    # Automatically set the date to now upon creation of a new attendance record
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)

    # ASSOCIATIVE RELATIONSHIP: Many students belong to many classes
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    joined_class = models.ForeignKey('Teacher.Class', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_attendances'
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'

        # Prevent duplicate attendance records from being created
        unique_together = ('student', 'joined_class', 'date')

    # Show attendance details in admin site
    def __str__(self):
        return f"{self.joined_class} - {self.student} - {self.date}"

