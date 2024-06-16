from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Rigg, Movementg
from datetime import datetime
from django.db import connection

# from .models import Rig


def members(request):
    template = loader.get_template("blog/home.html")
    return HttpResponse(template.render())


# def rig_list(request):
#     rigs = Rig.objects.all()  # Get all rigs, including their related engineers
#     return render(request, 'blog/rig_list.html', {'rigs': rigs})


# views.py


# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all()
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     return render(request, 'blog/rig_timeline1.html', {'rigs': rigs, 'movements': movements, "months":months})


# views.py


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


# def get_month_span(start_date, end_date):
#     start_month = start_date.month
#     end_month = end_date.month
#     year_span = end_date.year - start_date.year
#     month_span = end_month - start_month + 1 + (year_span * 12)
#     return month_span

# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all()
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     movement_spans = []
#     for movement in movements:
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span,
#             'start_month': movement.start_date.month
#         })

#     for x in movement_spans:
#         print(x)

#     return render(request, 'blog/rig_timeline1.html', {'rigs': rigs, 'movements': movement_spans, 'months': months})

from django.shortcuts import render
from .models import Rigg, Movementg
from datetime import datetime


from django.shortcuts import render
from .models import Rigg, Movementg

# def get_month_span(start_date, end_date):
#     """Calculate the number of months between two dates, inclusive."""
#     start_month = start_date.month
#     end_month = end_date.month
#     year_span = end_date.year - start_date.year
#     month_span = end_month - start_month + 1 + (year_span * 12)
#     return month_span

# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all()

#     # Define the list of months for display
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     # Define a range of years you want to cover
#     years = list(range(2024, 2031))  # Adjust the range as necessary

#     # Prepare the data for rendering
#     movement_spans = []
#     for movement in movements:
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span,
#             'start_month': movement.start_date.month,
#             'start_year': movement.start_date.year,
#             'end_year': movement.end_date.year
#         })
#         print(month_span)
#         zipped_data = zip(rigs, movements)


#     context = {
#         'rigs': rigs,
#         'movements': movement_spans,
#         'months': months,
#         'years': years,
#         'zipped_data': zipped_data
#     }
#     return render(request, 'blog/rig_timeline1.html', context)


# from here

# from django.shortcuts import render
# from .models import Rigg, Movementg
# from datetime import date

# def get_month_span(start_date, end_date):
#     """Calculate the number of months between two dates, inclusive."""
#     start_month = start_date.month
#     end_month = end_date.month
#     year_span = end_date.year - start_date.year
#     month_span = end_month - start_month + 1 + (year_span * 12)
#     return month_span

# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all()

#     # Define the list of months for display
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", ]

#     # Define a range of years you want to cover
#     years = list(range(2024, 2025))  # Adjust the range as necessary

#     # Prepare the data for rendering
#     movement_spans = []
#     for movement in movements:
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span,
#             'start_month': movement.start_date.month,
#             'start_year': movement.start_date.year,
#             'end_year': movement.end_date.year
#         })

#     context = {
#         'rigs': rigs,
#         'movements': movement_spans,
#         'months': months,
#         'years': years
#     }
#     return render(request, 'blog/rig_timeline1.html', context)


###### here ##########

# from django.shortcuts import render
# from .models import Rigg, Movementg
# from datetime import date

# def get_month_span(start_date, end_date):
#     """Calculate the number of months between two dates, inclusive."""
#     start_month = start_date.month
#     end_month = end_date.month
#     year_span = end_date.year - start_date.year
#     month_span = end_month - start_month + 1 + (year_span * 12)
#     print(month_span)
#     return month_span

# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all().order_by('start_date')

#     # Define the list of months for display
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     # Define a range of years you want to cover
#     years = list(range(2024, 2027))  # Adjust the range as necessary

#     # Prepare the data for rendering
#     movement_spans = []
#     for movement in movements:
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span,
#             'start_month': movement.start_date.month,
#             'start_year': movement.start_date.year,
#             'end_year': movement.end_date.year
#         })
#         print("=" * 33)
#         print(month_span)
#         for year in years:
#             print(year)

#     context = {
#         'rigs': rigs,
#         'movements': movement_spans,
#         'months': months,
#         'years': years
#     }


#     return render(request, 'blog/rig_timeline1.html', context)
# #######


def get_month_span(start_date, end_date):
    """Calculate the number of months between two dates, inclusive."""
    start_month = start_date.month
    end_month = end_date.month

    year_span = end_date.year - start_date.year
    month_span = end_month - start_month + 1 + (year_span * 12)
    print(month_span)

    return month_span


def get_month_span(start_date, end_date):
    return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1

def rig_timeline1(request):
    rigs = Rigg.objects.all()
    movements = Movementg.objects.all().order_by('start_date')
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    years = list(range(2024, 2027))  # Adjust the range as necessary

    movement_spans = []
    for movement in movements:
        month_span = get_month_span(movement.start_date, movement.end_date)
        start_month_index = (movement.start_date.year - years[0]) * 12 + (movement.start_date.month - 1)
        movement_spans.append({
            'rig': movement.rig,
            'well': movement.well,
            'start_date': movement.start_date,
            'end_date': movement.end_date,
            'month_span': month_span * 8.33,  # Width in percentage
            'start_month_index': start_month_index,  # Position in the calendar
        })

    context = {
        'rigs': rigs,
        'movements': movement_spans,
        'months': months,
        'years': years,
    }
    
    return render(request, 'blog/rig_timeline1.html', context)



# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all().order_by('start_date')
#     # print(movements)
#     # Define the list of months for display
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     # Define a range of years you want to cover
#     years = list(range(2024, 2027))  # Adjust the range as necessary

#     # Prepare the data for rendering
#     movement_spans = []

#     for movement in movements:
#         print(movement.start_date)
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span * 8.33,
#             'start_month': movement.start_date.month,
#             'start_year': movement.start_date.year,
#             'end_year': movement.end_date.year
#         })
#     projects = Project.objects.raw('SELECT id FROM "TRS_DRE2_project"')

#     context = {
#         'rigs': rigs,
#         'movements': movement_spans,
#         'months': months,
#         'years': years,
#         'projects': projects
#     }

#     return render(request, 'blog/rig_timeline1.html', context)


# def create_rig_info(request):
#     # Logic to create rig information
#     return render(request, 'blog/create_rig_info.html')

# def view_rig_info(request):
#     # Logic to view all rig information
#     return render(request, 'blog/view_rig_info.html')


# views.py


#  movement_new = []
#     for rig in rigs:
#         rig_movements = movements.filter(rig=rig).order_by('start_date')
#         for movement in rig_movements:
#             movement_year = movement.start_date.year
#             if movement_year in years:
#                 movement_month = movement.start_date.month
#                 month_name = months[movement_month - 1]
#                 print(f"Rig: {rig}, Start Date: {movement.start_date}, Year: {movement_year}, Month: {month_name}")
#                 month_span = get_month_span(movement.start_date, movement.end_date)
#                 movement_new.append({
#                     'rig': movement.rig,
#                     'well': movement.well,
#                     'start_date': movement.start_date,
#                     'end_date': movement.end_date,
#                     'month_span': month_span,
#                     'start_month': movement.start_date.month,
#                     'start_year': movement.start_date.year,
#                     'end_year': movement.end_date.year
#                 })
#         else:
#             movement_new.append({
#                 'rig': movement.rig,
#                 'well': 'None',
#                 'start_date': 'None',
#                 'end_date': 'None',
#                 'month_span': 'None',
#                 'start_month': 'None',
#                 'start_year': 'None',
#                 'end_year': 'None'
#             })
# for movement_n  in movement_new:
#     print(movement_n['well'])

# context = {
#     'rigs': rigs,
#     'movements': movement_new,
#     'months': months,
#     'years': years
# }

# return render(request, 'blog/rig_timeline1.html', context)


def create_rig_info(request):
    # Logic to create rig information
    return render(request, "blog/create_rig_info.html")


def view_rig_info(request):
    # Logic to view all rig information
    return render(request, "blog/view_rig_info.html")


from django.shortcuts import render
from datetime import timedelta


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
