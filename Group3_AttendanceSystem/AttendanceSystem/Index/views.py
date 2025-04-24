# Index Views
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import forms


def register_role_view(request):
    return render(request, 'registerrole.html')


def register_student_view(request):
    from .models import UserProfile, StudentProfile
    if request.method == 'POST':
        form = forms.StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile with role 'student'
            user_profile = UserProfile.objects.create(user=user, role='student')
            # Create StudentProfile with extra fields
            StudentProfile.objects.create(
                profile=user_profile,
                student_id=form.cleaned_data['student_id'],
                course=form.cleaned_data['course'],
                year=form.cleaned_data['year']
            )
            messages.success(request, 'Student account created successfully.')
            return redirect('loginrole')
        else:
            # Remove the generic messages.error call here
            # The template will now handle displaying specific errors
            pass # Keep the rest of the logic
    else:
        form = forms.StudentRegisterForm()
    # Ensure the form object is always passed to the template
    return render(request, 'registerstudent.html', {'form': form})


def register_teacher_view(request):
    from .models import UserProfile, TeacherProfile
    if request.method == 'POST':
        form = forms.TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile with role 'teacher'
            user_profile = UserProfile.objects.create(user=user, role='teacher')
            # Create TeacherProfile with extra fields
            TeacherProfile.objects.create(
                profile=user_profile,
                department_id=form.cleaned_data['department_id'],
                courses=form.cleaned_data['courses']
            )
            messages.success(request, 'Teacher account created successfully.')
            return redirect('loginrole')
        else:
            # Remove the generic messages.error call here
            # The template will now handle displaying specific errors
            pass # Keep the rest of the logic
    else:
        form = forms.TeacherRegisterForm()
    # Ensure the form object is always passed to the template
    return render(request, 'registerteacher.html', {'form': form})


def login_role_view(request):
    return render(request, 'loginrole.html')


def login_student_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user exists
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user has a student role
            try:
                if user.userprofile.role == 'student':
                    login(request, user)
                    return redirect('/student/newdashboard/')
                else:
                    messages.error(request, 'This account is not registered as a student.')
            except Exception as e:
                messages.error(request, f'User profile error: {str(e)}')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'loginstudent.html')


def login_teacher_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user exists
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user has a teacher role
            try:
                if user.userprofile.role == 'teacher':
                    login(request, user)
                    return redirect('/teacher/dashboard')
                else:
                    messages.error(request, 'This account is not registered as a teacher.')
            except Exception as e:
                messages.error(request, f'User profile error: {str(e)}')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'loginteacher.html')


# Render index page
class Index(View):
    def get(self, request):
        return render(request, 'index.html')


# Render login page
class Login(View):
    def get(self, request):
        return redirect('loginrole')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check if user exists
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect based on user role
                try:
                    role = user.userprofile.role
                    if role == 'student':
                        return redirect('/student/newdashboard/')  # Student dashboard URL
                    elif role == 'teacher':
                        return redirect('/teacher/dashboard')  # Teacher dashboard URL
                    else:
                        messages.error(request, 'User role not set.')
                        return redirect('loginrole')
                except Exception as e:
                    messages.error(request, f'User profile not found: {str(e)}')
                    return redirect('loginrole')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('loginrole')


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
