from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Teacher, Class
from Student.models import JoinRequest, Enrollment


# Create your views here.

class Dashboard(View):

    def get(self,request):
        username = request.session.get('user')
        teacher = Teacher.objects.get(username=username)
        cursor = connection.cursor()
        cursor.callproc('get_classes',[username])
        classlist = cursor.fetchall()
        cursor.close()
        return render(request, 'TeacherDashboard.html',{'teacher': teacher, 'classlist':classlist})


class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')


class classList(View):
    def get(self, request, class_id):
        cursor = connection.cursor()
        cursor.callproc('open_class',[class_id])
        students = cursor.fetchall()
        cursor.close()

        cursor = connection.cursor()
        cursor.callproc('get_pendingrequest', [class_id])
        pending_requests = cursor.fetchall()
        cursor.close()

        return render(request, 'class.html', {
            'class': class_id,
            'students': students,
            'pending_requests': pending_requests
        })

    def post(self, request, class_id):
        student_id = request.POST.get('student_id')
        action = request.POST.get('action')

        if student_id and action:
            if action == 'approve':
                cursor = connection.cursor()
                cursor.callproc('accept_request', [student_id, class_id])
                cursor.close()
            elif action == 'reject':
                cursor = connection.cursor()
                cursor.callproc('reject_request', [student_id, class_id])
                cursor.close()

        return redirect('classList', class_id=class_id)
