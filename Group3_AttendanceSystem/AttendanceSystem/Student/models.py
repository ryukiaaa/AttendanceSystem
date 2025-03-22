from django.db import models
from Index import models

# Create your models here.

class Student(User):
    student_id = models.CharField(max_length=20, primary_key=True)
    course = models.CharField(max_length=100)
    year_level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student_id}-{self.last_name}"


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
