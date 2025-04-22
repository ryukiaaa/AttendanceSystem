from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('studentDashboard', Dashboard.as_view(), name='studentDashboard'),
]