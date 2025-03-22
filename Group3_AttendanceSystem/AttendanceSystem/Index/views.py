from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):
    template_name = 'HomePage.html'

    def get(self,request):
        return render(request, 'HomePage.html')