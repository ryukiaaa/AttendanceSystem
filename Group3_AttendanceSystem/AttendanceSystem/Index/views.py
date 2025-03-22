from django.shortcuts import render, redirect
from django.views import View
from .models import User

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