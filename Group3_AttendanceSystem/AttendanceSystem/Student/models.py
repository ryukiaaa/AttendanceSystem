from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubtypeTest(User):
    year = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        first_name = super(User, self).first_name
        last_name = super(User, self).last_name
        return first_name + ' ' + last_name


class Student(User):
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    # Makes sure the password is hashed in the database when a new student is created
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    # Show firstname and lastname in admin site
    def __str__(self):
        # Get inherited fields
        first_name = super(User, self).first_name
        last_name = super(User, self).last_name

        return first_name + ' ' + last_name

    # Change displayed model name in admin site
    class Meta:
        verbose_name =  'student'
        verbose_name_plural = 'students'


class Attendance(models.Model):
    # When an attendance record is created, the date is automatically set to current date
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)

    # ASSOCIATION: Many students to many classes
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    joined_class = models.ForeignKey('Teacher.Class', on_delete=models.CASCADE)

    # Avoid duplicate (same student on the same class and date) attendance records
    class Meta:
        unique_together = ('student', 'joined_class', 'date')

    # Show attendance details in admin site
    def __str__(self):
        return f"{self.student} - {self.joined_class} on {self.date}"
