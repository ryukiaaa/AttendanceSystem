# Student Views
from django.shortcuts import render
from django.views import View

class StudentDashboard(View):
    def get(self, request):
        return render(request, 'studentdashboard.html')
