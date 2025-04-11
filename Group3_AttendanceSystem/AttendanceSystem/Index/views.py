# Authentication Views
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from . import forms
from .forms import CreateTeacherForm


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Login(View):
    def get(self, request):
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
                return redirect('index')
            else:
                messages.info(request, 'Invalid credentials')
                return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


# UNUSED: Old register page (creates supertype User)
class RegisterOld(View):
    form = forms.CreateUserForm()

    def get(self, request):
        return render(request, 'registerold.html', {'form':self.form})

    def post(self, request):
        if request.method == 'POST':
            form = forms.CreateUserForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                form.save()
                firstname = form.cleaned_data.get('first_name')
                lastname = form.cleaned_data.get('last_name')
                messages.success(request, 'New user ' + firstname + ' ' + lastname + ' has been created')
                return redirect('login')
            # If not, show error message and refresh the reset form fields
            else:
                messages.error(request, 'ERROR: All fields must be valid!')

                if len(form.cleaned_data.get('password')) < 8:
                    messages.error(request, 'Password must contain at least 8 characters')

                if form.cleaned_data.get('password') != form.cleaned_data.get('password2'):
                    messages.error(request, 'Passwords should match')

                return render(request, 'registerold.html', {'form': self.form})


class RegisterStudent(View):
    form = forms.CreateStudentForm()

    def get(self, request):
        return render(request, 'registerstudent.html', {'form': self.form})

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

                return render(request, 'registerstudent.html', {'form': self.form})


class RegisterTeacher(View):
    form = CreateTeacherForm()

    def get(self, request):
        return render(request, 'registerteacher.html', {'form': self.form})

    def post(self, request):
        if request.method == 'POST':
            form = forms.CreateTeacherForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                user = form.save()
                # Assign to 'Teacher' group to access student pages
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

                return render(request, 'registerteacher.html', {'form': self.form})
