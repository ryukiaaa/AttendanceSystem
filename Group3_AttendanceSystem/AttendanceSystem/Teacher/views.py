from django.shortcuts import render
from django.views import View
from .models import Teacher


# Create your views here.

class Dashboard(View):


    def get(self,request):
        teacher = Teacher.objects.get(pk=9034823)
        return render(request, 'TeacherDashboard.html', {'firstname': teacher.lastname})
