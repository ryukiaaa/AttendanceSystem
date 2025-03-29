# Index Views
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import forms


# Render index page
class Index(View):
    def get(self, request):
        return render(request, 'index.html')


# Render login page
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check if user exists
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('student:dashboard')
            else:
                messages.info(request, 'Invalid credentials')
                return render(request, 'login.html')


# Render register page
class Register(View):
    form = forms.CreateUserForm()

    def get(self, request):
        return render(request, 'register.html', {'form':self.form})

    def post(self, request):
        if request.method == 'POST':
            form = forms.CreateUserForm(request.POST)

            # Adds user to the database if all form fields are valid
            if form.is_valid():
                form.save()
                firstname = form.cleaned_data.get('first_name')
                lastname = form.cleaned_data.get('last_name')
                messages.success(request, 'New user ' + firstname + ' ' + lastname + ' has been created.')
                return redirect('login')
            # If not, show error message and refresh the reset form fields
            else:
                messages.error(request, 'ERROR: All fields must be valid!')

                if len(form.cleaned_data.get('password1')) < 8:
                    messages.error(request, 'Password must contain at least 8 characters')

                if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                    messages.error(request, 'Passwords should match')

                return render(request, 'register.html', {'form': self.form})
