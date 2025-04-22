from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('teacherDashboard', Dashboard.as_view(), name='teacherDashboard'),
]