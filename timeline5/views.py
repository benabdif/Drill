
# timeline/views.py

from django.shortcuts import render
from .models import Project

def project_timeline(request):
    projects = Project.objects.all().prefetch_related('phases')
    months = range(1, 13)  # List of months from 1 to 12
    
    return render(request, 'blog/project_timeline.html', {'projects': projects, 'months': months})
