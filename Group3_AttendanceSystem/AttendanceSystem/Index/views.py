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
        return redirect('student/dashboard')


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
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        type = 'S'
        return redirect('login')


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
            userCheck = User.objects.get(pk=username).exist()
            if userCheck:
                return render(request, 'registerstudent.html', {'form': self.form, 'message':'user already exist'})
            else:
                course = request.POST['course']
                year_level = request.POST['year_level']

                user = User.objects.create(
                    username=username,
                    password=password,
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    type=type
                )

                Student.objects.create(
                    user_ptr=user,
                    course=course,
                    year_level=year_level
                )
                return redirect('studentDashboard')

        except Exception as e:
            print("Error:", e)
            return render(request, 'registerstudent.html', {'form': self.form, 'message': 'error'})