# Teacher Views

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from . import models
from . import forms


class TeacherDashboard(View):
    def get(self, request):
        teacher = request.user
        return render(request, 'teacher_dashboard.html', {'teacher':teacher})


class CreateClass(View):
    form = forms.CreateClassForm()

    def get(self, request):
        teacher = request.user
        return render(request, 'create_class.html', {'form':self.form, 'teacher':teacher})

    def post(self, request):
        teacher = request.user

        if request.method == 'POST':
            form = forms.CreateClassForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                new_class = form.save(commit=False)
                # Assign currently logged in teacher to the class
                new_class.teacher = models.Teacher.objects.get(user_ptr_id=request.user)
                new_class.save()
                return render(request, 'create_class.html', {'form': self.form, 'teacher':teacher})

        return None


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
