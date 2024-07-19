from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project
from datetime import datetime, date
from django.utils import timezone
from django.db import connection
# Create your views here.

def members2(request):
    template = loader.get_template('blog/home2.html')
    return HttpResponse(template.render())




# def project_timeline(request):
#     projects = Project.objects.all()
#     return render(request, 'blog/timeline.html', {'projects': projects})

# rigs/views.py

def project_timeline(request):
    projects = Project.objects.raw('SELECT id FROM "TRS_DRE2_project"')
    
    return render(request, 'blog/timeline.html', {'projects': projects})


# fadhel
def rig_schedule(request):
    wieth = 100 / 12

    rigs = Project.objects.all()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    rig_data = []
    active_number = []
    fadhel = []

    for rig in rigs:
        start_month = rig.start_date.month
        # print(start_month)
        end_month = rig.end_date.month
        # print(end_month)
        month_active = [0] * 12  # 12 months, initialized to 0
        for i in range(start_month - 1, end_month):
            month_active[i] = 1  # Set active months to 1
        # Create ranges for active months
        active_ranges = []

        start = None
        for i, active in enumerate(month_active):
            if active and start is None:
                start = i  # Start of a new active range
            elif not active and start is not None:
                # End of an active range
                active_ranges.append((start, i - start))
                start = None
        if start is not None:
            # If the last month(s) are active
            active_ranges.append((start, 12 - start))

        rig_data.append((rig, active_ranges))

        second_numbers = [t[1] for t in active_ranges]
        # print(second_numbers)
        numptnumber = [float(num) * (100/12) for num in second_numbers]
        active_number.append(numptnumber)

        # active_number.append(numptnumber)
        # print(len(active_number))

    return render(request, 'blog/home3.html', {'rig_data': rig_data, 'months': months, 'active_number':active_number})
# fadhel


def rig_schedule1(request):
    wieth = 100 / 12
    rigs = Project.objects.all()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    
    return render(request, 'blog/home6.html', {})

    






# ********This code Activeted********** 

 



# def rig_schedule(request):
#     rigs = Project.objects.all()  # Consider using select_related or prefetch_related if joining other tables
#     months = ['January', 'February', 'March', 'April', 'May', 'June', 
#               'July', 'August', 'September', 'October', 'November', 'December']
#     current_year = timezone.now().year  # Use the current year, or adapt as necessary
#     rig_data = []

#     for rig in rigs:
#         if rig.start_date and rig.end_date:  # Check if dates are not None
#             start_month = rig.start_date.month
#             end_month = rig.end_date.month
#             start_year = rig.start_date.year
#             end_year = rig.end_date.year

#             # Initialize months as inactive
#             month_active = [0]*12

#             # If the project spans multiple years, adjust the logic
#             if start_year == current_year and end_year == current_year:
#                 for i in range(start_month - 1, end_month):
#                     month_active[i] = 1
#             elif start_year < current_year and end_year == current_year:
#                 for i in range(0, end_month):
#                     month_active[i] = 1
#             elif start_year == current_year and end_year > current_year:
#                 for i in range(start_month - 1, 12):
#                     month_active[i] = 1

#             rig_data.append((rig, month_active))

#     return render(request, 'blog/home3.html', {'rig_data': rig_data, 'months': months})




def sql_file(request):
    mysql = Project.objects.raw('SELECT name, well FROM "TRS_DRE2_project"')
    color = 25

    # print(list(mysql))
    return render(request, 'blog/sql_f.html', {'mysql': mysql, 'color':color})












# def project_timeline(request):
#     projects = Project.objects.all()
#     for project in projects:
#         # Calculate grid start and end points
#         project.grid_column_start = project.start_date.month
#         project.grid_column_end = project.end_date.month + 1  # Include the next month as end point for CSS grid
#     return render(request, 'blog/project_timeline.html', {'projects': projects, 'months': range(1, 13)})



