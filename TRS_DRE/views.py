from django.shortcuts import render
# from django.http import HttpResponse
from django.template import loader
from datetime import timedelta
from .models import Rigg, Movementg, Wellg
from datetime import datetime
from django.db import connection
from django.db.models import Min, Max







def get_projects_with_month_diff():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                id,
                name,
                start_date, 
                end_date,
                (DATE_PART('year', age(end_date, start_date)) * 12 + DATE_PART('month', age(end_date, start_date))) AS month_diff
            FROM 
                public."TRS_DRE2_project"
            ORDER BY 
                id ASC;
        """)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results


def project_list(request):
    projects = get_projects_with_month_diff()
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return render(
        request,
        "blog/project_list.html",
        {
            "projects": projects,
            "months": months,
        },
    )







def rig_timeline1(request):
    
    riggs = Rigg.objects.prefetch_related("movementg_set").all()
    RIGG1 = Rigg.objects.all()
    RIGG2 = Wellg .objects.all()
    field_type_choices = Rigg.FIELD_TYPE_CHOICES    
    
    if riggs:
        earliest_start_date = Movementg.objects.aggregate(Min("start_date"))[
            "start_date__min"
        ]
        latest_end_date = Movementg.objects.aggregate(Max("end_date"))["end_date__max"]
        years = list(range(earliest_start_date.year, latest_end_date.year + 1))
        total_products = riggs.count()

        context = {
            "riggs": riggs,
            "years": years,
            'earliest_start_date': earliest_start_date,
            'field_type_choices' : field_type_choices,
            'total_products':total_products
        }
        return render(request, "blog/rig_timeline1.html", context or {})

    return render(request, "blog/rig_timeline1.html")



def create_rig_info(request):
    # Logic to create rig information
    return render(request, "blog/create_rig_info.html")


def view_rig_info(request):
    # Logic to view all rig information
    return render(request, "blog/view_rig_info.html")




def your_view(request):
    # Fetch rigs, movements, years, months from your models
    rigs = Rigg.objects.all()
    years = [2023, 2024, 2025]  # Example years
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    movements = Movementg.objects.all()

    # Calculate is_contiguous property for movements
    for rig in rigs:
        rig_movements = movements.filter(rig=rig).order_by("start_date")
        for i in range(1, len(rig_movements)):
            previous_movement = rig_movements[i - 1]
            current_movement = rig_movements[i]
            if (
                previous_movement.end_date + timedelta(days=1)
                == current_movement.start_date
            ):
                current_movement.is_contiguous = True
            else:
                current_movement.is_contiguous = False

    context = {
        "rigs": rigs,
        "years": years,
        "months": months,
        "movements": movements,
    }
    return render(request, "your_template.html", context)
