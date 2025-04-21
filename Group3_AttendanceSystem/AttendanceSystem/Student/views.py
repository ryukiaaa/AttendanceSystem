# Student Views

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout


class StudentDashboard(View):
    def get(self, request):
        return render(request, 'student_dashboard.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
