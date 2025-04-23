from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('Dashboard', Dashboard.as_view(), name='studentDashboard'),
]