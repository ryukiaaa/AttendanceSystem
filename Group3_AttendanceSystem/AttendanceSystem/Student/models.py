from django.db import models
from Index.models import User
from Teacher.models import Class
import uuid
# Create your models here.

class Student(User):
    student_id = models.CharField(max_length=20, primary_key=True)
    course = models.CharField(max_length=100)
    year_level = models.PositiveIntegerField()
    joined_class = models.ManyToManyField(Class, through="Enrollment")

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id}-{self.lastname}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'class_obj', 'date')

    def __str__(self):
        return f"{self.student} - {self.class_obj} on {self.date}"


class JoinRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'class_obj', 'status')

    def __str__(self):
        return f"{self.student} requested {self.class_obj} - {self.status}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'class_obj')

    def __str__(self):
        return f"{self.student} enrolled in {self.class_obj}"
