from django.urls import path
from .views import Dashboard, EmptyTeacherDashboardView

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('empty-dashboard', EmptyTeacherDashboardView.as_view(), name='empty_dashboard'),
]