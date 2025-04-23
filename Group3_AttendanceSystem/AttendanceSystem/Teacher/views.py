from django.shortcuts import render, redirect
from django.views import View
from .models import Teacher


# Create your views here.

class Dashboard(View):

    def get(self,request):
        username = request.session.get('user')
        teacher = Teacher.objects.get(username=username)
        return render(request, 'TeacherDashboard.html',{'teacher': teacher})


class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')