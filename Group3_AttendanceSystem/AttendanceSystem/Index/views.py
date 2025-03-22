from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):

    def get(self,request):
        return render(request, 'HomePage.html')


class Login(View):

    def get(self,request):
        return render(request, 'login.html')