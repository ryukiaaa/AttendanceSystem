from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.views import View
from . import forms

# Create your views here.

class Index(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            return redirect('student:dashboard')
        elif request.user.is_authenticated and request.user.groups.filter(name='Teacher').exists():
            return redirect('teacher:dashboard')
        else:
            return render(request, 'index.html')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            return redirect('student:dashboard')
        elif request.user.is_authenticated and request.user.groups.filter(name='Teacher').exists():
            return redirect('teacher:dashboard')
        else:
            return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.groups.filter(name='Student').exists():
                login(request, user)
                return redirect('student:dashboard')
            elif user is not None and user.groups.filter(name='Teacher').exists():
                login(request, user)
                return redirect('teacher:dashboard')
            else:
                messages.info(request, 'Invalid credentials')
                return render(request, 'login.html')

        return None


class Register(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            return redirect('student:dashboard')
        elif request.user.is_authenticated and request.user.groups.filter(name='Teacher').exists():
            return redirect('teacher:dashboard')
        else:
            return render(request, 'register.html')


class RegisterStudent(View):
    form = forms.CreateStudentForm()

    def get(self, request):
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            return redirect('student:dashboard')
        elif request.user.is_authenticated and request.user.groups.filter(name='Teacher').exists():
            return redirect('teacher:dashboard')
        else:
            return render(request, 'register_student.html', {'form': self.form})

    def post(self, request):
        if request.method == 'POST':
            form = forms.CreateStudentForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                user = form.save()
                # Assign to 'Student' group to access student pages
                user.groups.add(Group.objects.get(name='Student'))
                firstname = form.cleaned_data.get('first_name')
                lastname = form.cleaned_data.get('last_name')
                messages.success(request, 'New student ' + firstname + ' ' + lastname + ' has been created')
                return redirect('login')
            # If not, show error message and reset the form fields
            else:
                messages.error(request, 'ERROR: All fields must be valid!')

                if len(form.cleaned_data.get('password')) < 8:
                    messages.error(request, 'Password must contain at least 8 characters')

                if form.cleaned_data.get('password') != form.cleaned_data.get('password2'):
                    messages.error(request, 'Passwords should match')

                return render(request, 'register_student.html', {'form': self.form})

        return None


class RegisterTeacher(View):
    form = forms.CreateTeacherForm()

    def get(self, request):
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            return redirect('student:dashboard')
        elif request.user.is_authenticated and request.user.groups.filter(name='Teacher').exists():
            return redirect('teacher:dashboard')
        else:
            return render(request, 'register_teacher.html', {'form': self.form})

    def post(self, request):
        if request.method == 'POST':
            form = forms.CreateTeacherForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                user = form.save()
                # Assign to 'Teacher' group to access teacher pages
                user.groups.add(Group.objects.get(name='Teacher'))
                firstname = form.cleaned_data.get('first_name')
                lastname = form.cleaned_data.get('last_name')
                messages.success(request, 'New teacher ' + firstname + ' ' + lastname + ' has been created')
                return redirect('login')
            # If not, show error message and reset the form fields
            else:
                messages.error(request, 'ERROR: All fields must be valid!')

                if len(form.cleaned_data.get('password')) < 8:
                    messages.error(request, 'Password must contain at least 8 characters')

                if form.cleaned_data.get('password') != form.cleaned_data.get('password2'):
                    messages.error(request, 'Passwords should match')

                return render(request, 'register_teacher.html', {'form': self.form})

        return None
