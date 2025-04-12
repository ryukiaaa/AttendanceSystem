# Student Views
from django.shortcuts import render
from django.views import View
from django.shortcuts import render

class StudentDashboard(View):
    def get(self, request):
        return render(request, 'studentdashboard.html')

class NewStudentDashboard(View):
    def get(self, request):
        return render(request, 'newstudentdashboard.html')
