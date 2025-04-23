from django.shortcuts import render, redirect
from django.views import View
from .models import User
from Student.models import Student
from Teacher.models import Teacher
from . import forms

# Create your views here.

class Home(View):

    def get(self,request):
        return render(request, 'HomePage.html')

    def post(self, request):
        if request.POST.get('action') == 'login':
            return redirect('login')
        elif request.POST.get('action') == 'register':
            return redirect('register')


class Login(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)

            if user.password != password:
                return render(request, 'login.html', {'message': 'Invalid password'})

            if user.type == 'S':
                try:
                    student = Student.objects.get(username=username)
                    request.session['user'] = username
                    request.session['user_type'] = 'student'
                    return redirect('studentDashboard')
                except Student.DoesNotExist:
                    return render(request, 'login.html', {'message': 'Student not found'})

            elif user.type == 'T':
                try:
                    teacher = Teacher.objects.get(username=username)
                    request.session['user'] = username
                    request.session['user_type'] = 'teacher'
                    return redirect('teacherDashboard')
                except Teacher.DoesNotExist:
                    return render(request, 'login.html', {'message': 'Teacher not found'})

            else:
                return render(request, 'login.html', {'message': 'Invalid user type'})

        except User.DoesNotExist:
            return render(request, 'login.html', {'message': 'User does not exist'})


class Register(View):

    def get(self,request):
        return render(request, 'register.html')

    def post(self, request):
        return redirect('login')


class RegisterTeacher(View):
    form = forms.CreateTeacherForm()

    def get(self,request):
        return render(request, 'registerteacher.html',{'form': self.form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        type = 'T'

        try:
            userCheck = User.objects.filter(pk=username).exists()
            if userCheck:
                return render(request, 'registerteacher.html', {'form': self.form, 'message': 'user already exist'})
            else:
                department = request.POST['department']

                Teacher.objects.create(
                    username=username,
                    password=password,
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    type=type,
                    department=department
                )
                return redirect('login')

        except Exception as e:
            print("Error:", e)
            return render(request, 'registerteacher.html', {'form': self.form, 'message': e})


class RegisterStudent(View):
    form = forms.CreateStudentForm()

    def get(self,request):
        return render(request, 'registerstudent.html', {'form': self.form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        type = 'S'

        try:
            userCheck = User.objects.filter(pk=username).exists()
            if userCheck:
                return render(request, 'registerstudent.html', {'form': self.form, 'message':'user already exist'})
            else:
                course = request.POST['course']
                year = request.POST['year']

                Student.objects.create(
                    username=username,
                    password=password,
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    type=type,
                    course=course,
                    year_level=year
                )
                return redirect('login')

        except Exception as e:
            print("Error:", e)
            return render(request, 'registerstudent.html', {'form': self.form, 'message': e})