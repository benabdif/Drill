from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader
from datetime import timedelta
from .models import (
    Rigg,
    Movementg,
    # Wellg,
    Construction_Departmeent,
    Pre_Construction,
    Well_Construction_Info,
)
# from datetime import datetime
from django.db import connection
from django.db.models import Min, Max
# from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


####################################################################
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from .models import Pre_Construction


def get_pre_construction_data(request):
    well_id = request.GET.get("well_id")

    # Assuming well_id is associated with the Pre_Construction model (this may vary based on your logic)
    pre_construction_data = get_object_or_404(Pre_Construction, well_id=well_id)

    # Return the necessary fields as JSON
    data = {
        "Approval_Status": pre_construction_data.Approval_Status,
        "Approval_Date": pre_construction_data.Approval_Date,
        "CONDTR_REQ": pre_construction_data.CONDTR_REQ,
        "R_Completio_Date": pre_construction_data.R_Completio_Date,
        "Approved_Lay_out": pre_construction_data.Approved_Lay_out,
        "Date_Approved_Lay_out": pre_construction_data.Date_Approved_Lay_out,
    }

    return JsonResponse(data)


#####################################################################


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
            "earliest_start_date": earliest_start_date,
            "field_type_choices": field_type_choices,
            "total_products": total_products,
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


def getMyinfo(request, pk):
    constructore_info = get_object_or_404(Construction_Departmeent, pk=pk)
    return render(
        request, "blog/rig_timeline1.html", {"constructore_info": constructore_info}
    )


def getMyinfo_JAX(request, pk):
    constructore_info = get_object_or_404(Construction_Departmeent, pk=pk)
    return render(
        request, "blog/rig_timeline1.html", {"constructore_info": constructore_info}
    )


# This is the function that get all the information
def get_Well_Construction_Info(request, pk):
    construction_info = get_object_or_404(Well_Construction_Info, pk=pk)
    
    return JsonResponse(
        {
            "name": construction_info.well_construction_name,  
            "objective": construction_info.well_construction_objective,
            "BI": construction_info.well_construction_BI,
            "Spud_date": construction_info.well_construction_Spud_date,
            "Reference_Number": construction_info.well_construction_Reference_Number,
            "well_construction_DWO_Engineer": construction_info.well_construction_DWO_Engineer,
            "well_construction_Producing_Engineer": construction_info.well_construction_Producing_Engineer,
            "Drillsite_Name": construction_info.well_construction_Drillsite_Name,
            "fluid_Type_choices": construction_info.well_construction_fluid_Type_choices,
            "Charge_Account": construction_info.well_construction_Charge_Account,
            "Released_date": construction_info.well_construction_Released_date,
            "well_construction_Direct_distance_DH": construction_info.well_construction_Direct_distance_DH,
            "Engineering_department": construction_info.well_construction_Engineering_department,
            "well_construction_GOSP_WIP_Department": construction_info.well_construction_GOSP_WIP_Department,
        }
    )

def get_Rig_Construction_Info(request, pk):
    Rig_construction_info = get_object_or_404(Rigg, pk=pk)
    
    return JsonResponse(
        {
            "Rig_name": Rig_construction_info.Rig_name,
            "Rig_Type": Rig_construction_info.Rig_Type,
            "Operation_Department": Rig_construction_info.Operation_Department,
            "Operation_Manager": Rig_construction_info.Operation_Manager,
            "Permanent_Construction_Cc": Rig_construction_info.Permanent_Construction_Cc,
            "Last_Update_Permanent_Construction_Cc": Rig_construction_info.Last_Update_Permanent_Construction_Cc, 
            "Permanent_HDPE_Contractor":Rig_construction_info.Permanent_HDPE_Contractor,
            "Last_Update_Permanent_HDPE_Contractor": Rig_construction_info.Last_Update_Permanent_HDPE_Contractor,
            "Permanent_Soil_Test_Contractor": Rig_construction_info.Permanent_Soil_Test_Contractor,
            "Last_Update_Permanent_Soil_Test_Contractor": Rig_construction_info.Last_Update_Permanent_Soil_Test_Contractor,
            "Current_Assigned_Unit": Rig_construction_info.Current_Assigned_Unit,
            "Current_Assigned_WS_Engineer": Rig_construction_info.Current_Assigned_WS_Engineer,


        }
    )
    


def save_note(request):
    if request.method == "POST":
        movement_id = request.POST.get("movement_id")
        note_text = request.POST.get("note")
        print(note_text)
        # Fetch the Movementg instance
        movement = get_object_or_404(Movementg, id=movement_id)

        # Update the note
        movement.note = note_text
        movement.save()

        return JsonResponse(
            {"status": "success", "message": "Note saved successfully!"}
        )
    else:
        return JsonResponse(
            {"status": "error", "message": "Invalid request"}, status=400
        )


######


def mytest_o(request):
    # Get all Pre_Construction objects
    Pre_Con = Pre_Construction.objects.all()

    # Extract the Approval_Status field from each object
    approval_status_list = Pre_Con.values_list("Approval_Status", flat=True)

    # Pass the list of approval statuses to the template
    context = {
        "Approval_Status": approval_status_list,
    }

    return render(request, "blog/test_o.html", context)
