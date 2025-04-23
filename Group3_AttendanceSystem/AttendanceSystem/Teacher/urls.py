from django.urls import path
from .views import Dashboard, Logout

urlpatterns = [
    path('Dashboard', Dashboard.as_view(), name='teacherDashboard'),
    path('Logout', Logout.as_view(), name='logout'),
]