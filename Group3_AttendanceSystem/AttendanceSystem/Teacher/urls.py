from django.urls import path
from .views import Dashboard, Logout, classList

urlpatterns = [
    path('Dashboard', Dashboard.as_view(), name='teacherDashboard'),
    path('Logout', Logout.as_view(), name='logout'),
    path('Class/<str:class_id>', classList.as_view(), name='classList'),
]