from django.shortcuts import render, redirect
from django.views import View
from .models import User

# Create your views here.

class Home(View):

    def get(self,request):
        return render(request, 'HomePage.html')



class Login(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self, request):
        return redirect('student/dashboard')