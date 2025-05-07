from django.contrib import admin
from .models import Student, Enrollment, JoinRequest

# Register your models here.
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(JoinRequest)