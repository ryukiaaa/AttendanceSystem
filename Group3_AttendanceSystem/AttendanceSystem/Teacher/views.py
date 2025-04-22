from django.shortcuts import render
from django.views import View


# Create your views here.
class Dashboard(View):
    """
    Main dashboard view for teachers.
    """
    def get(self, request):
        """Handle GET requests to display the teacher dashboard."""
        # This will be replaced with the actual dashboard once implemented
        return render(request, 'EmptyTeacherDashboard.html')

class EmptyTeacherDashboardView(View):
    """
    View for rendering the empty teacher dashboard template.
    This dashboard is shown when a teacher has no classes or attendance data yet.
    """
    def get(self, request):
        """Handle GET requests to display the empty teacher dashboard."""
        return render(request, 'EmptyTeacherDashboard.html')
