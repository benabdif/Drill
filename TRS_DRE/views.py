from django.shortcuts import render
from django.db.models.fields.files import FieldFile

from auditlog.models import LogEntry
from TRS_DRE.models import Movementg
from django.forms.models import model_to_dict

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
    Cellar,
    HDPE_Installation,
    Rig_Move,
    location_Support,
    Clean_Up_Section,
    RepairSection,
)

# from datetime import datetime
from django.db import connection
from django.db.models import Min, Max

# from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


####################################################################
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
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


# Well Construction (1)
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


# Rig Construction (2)
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
            "Permanent_HDPE_Contractor": Rig_construction_info.Permanent_HDPE_Contractor,
            "Last_Update_Permanent_HDPE_Contractor": Rig_construction_info.Last_Update_Permanent_HDPE_Contractor,
            "Permanent_Soil_Test_Contractor": Rig_construction_info.Permanent_Soil_Test_Contractor,
            "Last_Update_Permanent_Soil_Test_Contractor": Rig_construction_info.Last_Update_Permanent_Soil_Test_Contractor,
            "Current_Assigned_Unit": Rig_construction_info.Current_Assigned_Unit,
            "Current_Assigned_WS_Engineer": Rig_construction_info.Current_Assigned_WS_Engineer,
        }
    )


def get_Location_Map():
    pass


def get_Pre_Construction_Info(request, pk):
    Pre_Construction_Info = get_object_or_404(Pre_Construction, pk=pk)

    return JsonResponse(
        {
            "Approval_Status": Pre_Construction_Info.Approval_Status,
            "Approval_Date": Pre_Construction_Info.Approval_Date,
            "CONDTR_REQ": Pre_Construction_Info.CONDTR_REQ,
            "Approved_Lay_out": Pre_Construction_Info.Approved_Lay_out,
            "Date_Approved_Lay_out": Pre_Construction_Info.Date_Approved_Lay_out,
            "R_Completio_Date": Pre_Construction_Info.R_Completio_Date,
        }
    )


def get_Construction_Department(request, pk):
    # Correct model and function name
    Construction_Department_Info = get_object_or_404(Construction_Departmeent, pk=pk)

    return JsonResponse(
        {
            "CONSTR_REQ": Construction_Department_Info.CONSTR_REQ,
            "REQ_Start_Date": Construction_Department_Info.REQ_Start_Date,
            "REQ_Status": Construction_Department_Info.REQ_Status,
            "CONSTR_Contractor": Construction_Department_Info.CONSTR_Contractor,
            "CONSTR_KPI": Construction_Department_Info.CONSTR_KPI,
            "CONSTR_KOM": Construction_Department_Info.CONSTR_KOM,
            "Conducted_by_KOM": Construction_Department_Info.Conducted_by_KOM,
            "Construction_Status": Construction_Department_Info.Construction_Status,
            "CONSTR_Skid_ROAD_DIST": Construction_Department_Info.CONSTR_Skid_ROAD_DIST,
            "Final_Survey": Construction_Department_Info.Final_Survey,
            "Conducted_by_Final_Survey": Construction_Department_Info.Conducted_by_Final_Survey,
            "Unit": Construction_Department_Info.Unit,
            "Post_CONSTR_Rurn_OVER": Construction_Department_Info.Post_CONSTR_Rurn_OVER,  # Corrected "Rurn" to "Turn"
            "REQ_End_Date": Construction_Department_Info.REQ_End_Date,
            "Quanatities_Detities": Construction_Department_Info.Quanatities_Detities,  # Corrected "Quanatities_Detities"
            "Project_team_Details": Construction_Department_Info.Project_team_Details,
            "Remark_and_Hold": Construction_Department_Info.Remark_and_Hold,
            "Criticality": Construction_Department_Info.Criticality,
        }
    )


# def get_Cellar(request, pk):
#     Cellar_Info = get_object_or_404(Cellar, pk=pk)
#     return JsonResponse(
#         {
#             "Cellar_Installation": Cellar_Info.Cellar_Installation,
#             "Soil_Test_Request": Cellar_Info.Soil_Test_Request,
#             "REQ_Date": Cellar_Info.REQ_Date,
#             "Cellar_REQ_Status": Cellar_Info.Cellar_REQ_Status,
#             "Soil_Test_Contractor": Cellar_Info.Soil_Test_Contractor,
#             "Conducted_by": Cellar_Info.Conducted_by,
#         }
#     )

# I I have to fiux this problem I make this with
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Cellar


@csrf_exempt  # This allows POST requests without CSRF token (use carefully)
def get_Cellar(request, pk=None):
    if request.method == "GET":
        # Fetch existing data for a given primary key
        Cellar_Info = get_object_or_404(Cellar, pk=pk)
        return JsonResponse(
            {
                "id": Cellar_Info.pk,
                "Cellar_Installation": Cellar_Info.Cellar_Installation,
                "Soil_Test_Request": Cellar_Info.Soil_Test_Request,
                "REQ_Date": Cellar_Info.REQ_Date,
                "Cellar_REQ_Status": Cellar_Info.Cellar_REQ_Status,
                "Soil_Test_Contractor": Cellar_Info.Soil_Test_Contractor,
                "Conducted_by": Cellar_Info.Conducted_by,
            }
        )

    elif request.method == "POST":
        print(pk)
        data = request.POST
        Cellar.objects.filter(id=pk).update(
            Cellar_Installation=data.get("Cellar_Installation"),
            Soil_Test_Request=data.get("Soil_Test_Request"),
            REQ_Date=data.get("REQ_Date"),
            Cellar_REQ_Status=data.get("Cellar_REQ_Status"),
            Soil_Test_Contractor=data.get("Soil_Test_Contractor"),
            Conducted_by=data.get("Conducted_by"),
        )
        # Get data from the request body (POST)
        Cellar_Info = Cellar.objects.create(
            Cellar_Installation=data.get("Cellar_Installation"),
            Soil_Test_Request=data.get("Soil_Test_Request"),
            REQ_Date=data.get("REQ_Date"),
            Cellar_REQ_Status=data.get("Cellar_REQ_Status"),
            Soil_Test_Contractor=data.get("Soil_Test_Contractor"),
            Conducted_by=data.get("Conducted_by"),
        )
        return JsonResponse(
            {"message": "Cellar information added successfully!"}, status=201
        )


def get_HDPE_Installation(request, pk):
    HDPE_Installation_Info = get_object_or_404(HDPE_Installation, pk=pk)
    return JsonResponse(
        {
            "Lining_Installation": HDPE_Installation_Info.Lining_Installation,
            "REQ_Lining_Number": HDPE_Installation_Info.REQ_Lining_Number,
            "HDPE_REQ_Date": HDPE_Installation_Info.HDPE_REQ_Date,
            "HDPE_REQ_Status": HDPE_Installation_Info.HDPE_REQ_Status,
            "Installation_Status": HDPE_Installation_Info.Installation_Status,
            "Total_Area_Installed": HDPE_Installation_Info.Total_Area_Installed,
            "Lining_Contractor": HDPE_Installation_Info.Lining_Contractor,
            "Conducted_by_info": HDPE_Installation_Info.Conducted_by_info,
            "Quantities_Details": HDPE_Installation_Info.Quantities_Details,
        }
    )


def Get_Rig_Move(request, pk):
    Rig_Move_Info = get_object_or_404(Rig_Move, pk=pk)

    # Handle file field, check if file exists
    rig_move_documents_url = (
        Rig_Move_Info.RIG_MOVE_DOCUMENTS.url
        if Rig_Move_Info.RIG_MOVE_DOCUMENTS
        else None
    )

    return JsonResponse(
        {
            "RIG_MOVE_REQ": Rig_Move_Info.RIG_MOVE_REQ,
            "RIG_MOVE_NAME": Rig_Move_Info.RIG_MOVE_NAME,
            "RIG_MOVE_WELL": Rig_Move_Info.RIG_MOVE_WELL,
            "RIG_MOVE_STATUS": Rig_Move_Info.RIG_MOVE_STATUS,
            "RIG_MOVE_DOCUMENTS": rig_move_documents_url,
            "RIG_MOVE_CONDUCTED_BY": Rig_Move_Info.RIG_MOVE_CONDUCTED_BY,
        }
    )


def Get_Repair_Section(request, pk):
    # Fetch the RepairSection object using the primary key (pk)
    Repair_Section_info = get_object_or_404(RepairSection, pk=pk)

    # Return the required information in a JSON response
    return JsonResponse(
        {
            "REQ_Repair_NUMBER": Repair_Section_info.REQ_Repair_NUMBER,
            "REQ_Repair_Status": Repair_Section_info.REQ_Repair_Status,
            "REQ_Repair_Date": Repair_Section_info.REQ_Repair_Date,
            "Contractor_Contractor_Repair": Repair_Section_info.Contractor_Contractor_Repair,
            "Repair_Start_Date": Repair_Section_info.Repair_Start_Date,
            "Repair_status": Repair_Section_info.Repair_status,
            "Repair_completion_Date": Repair_Section_info.Repair_completion_Date,
            "monitored_By_Repair": Repair_Section_info.monitored_By_Repair,
            "Quantities_Details_Repair": Repair_Section_info.Quantities_Details_Repair,
            "Project_team_Details_Repair": Repair_Section_info.Project_team_Details_Repair,
            "sand_removal": Repair_Section_info.sand_removal,
            "Extension": Repair_Section_info.Extension,
            "Re_Compaction": Repair_Section_info.Re_Compaction,
            "Change_Cellar": Repair_Section_info.Change_Cellar,
            "Modification": Repair_Section_info.Modification,
            "Complete_Repair": Repair_Section_info.Complete_Repair,
            "Additional": Repair_Section_info.Additional,
        }
    )


def Get_Clean_Up_Section(request, pk):
    # Fetch the RepairSection object using the primary key (pk)
    Clean_Up_Section_info = get_object_or_404(Clean_Up_Section, pk=pk)

    # Return the required information in a JSON response
    return JsonResponse(
        {
            "clean_up_request_Number": Clean_Up_Section_info.clean_up_request_Number,
            "clean_up_request_Date": Clean_Up_Section_info.clean_up_request_Date,
            "clean_up_request_Status": Clean_Up_Section_info.clean_up_request_Status,
            "clean_up_construction_contractor": Clean_Up_Section_info.clean_up_construction_contractor,
            "clean_up_KPI": Clean_Up_Section_info.clean_up_KPI,
            "clean_up_start_Date": Clean_Up_Section_info.clean_up_start_Date,
            "clean_Up_start_Status": Clean_Up_Section_info.clean_Up_start_Status,
            "clean_up_completion_date": Clean_Up_Section_info.clean_up_completion_date,
            "clean_up_post_clean_Up_Turnover": Clean_Up_Section_info.clean_up_post_clean_Up_Turnover,
            "clean_up_monitored_by": Clean_Up_Section_info.clean_up_monitored_by,
            "clean_up_Quantities_details": Clean_Up_Section_info.clean_up_Quantities_details,
            "clean_up_project_team_details": Clean_Up_Section_info.clean_up_project_team_details,
            "clean_up_pre_Clean_Up_Turnover": Clean_Up_Section_info.clean_up_pre_Clean_Up_Turnover,
            "clean_up_Criticality": Clean_Up_Section_info.clean_up_Criticality,
        }
    )


def Get_location_Support(request, pk):
    location_Support_info = get_object_or_404(location_Support, pk=pk)
    return JsonResponse(
        {
            "on_location_support_Request_Number": location_Support_info.on_location_support_Request_Number,
            "on_location_support_Request_date": location_Support_info.on_location_support_Request_date,
            "on_location_support_Request_status": location_Support_info.on_location_support_Request_status,
            "on_location_support_contractor": location_Support_info.on_location_support_contractor,
            "on_location_support_dispatch_By": location_Support_info.on_location_support_dispatch_By,
            "on_location_support_Remark": location_Support_info.on_location_support_Remark,
        }
    )


from django.http import JsonResponse
from django.shortcuts import render
from .models import Well_Construction_Info, Rig_Move


def well_list(request):
    wells = (
        Well_Construction_Info.objects.all()
    )  # Fetch all wells to display in the list
    return render(request, "blog/rig_timeline1.html", {"wells": wells})


def get_rigs_for_well(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        well_id = request.GET.get("well_id", None)
        if well_id:
            well = Well_Construction_Info.objects.get(
                pk=well_id
            )  # Get the well based on the ID
            rigs = (
                well.rig_moves.all()
            )  # Get all rig moves related to the selected well

            # Prepare the data for JSON response
            rigs_data = list(
                rigs.values("RIG_MOVE_NAME", "RIG_MOVE_STATUS", "RIG_MOVE_CONDUCTED_BY")
            )
            return JsonResponse({"rigs": rigs_data})

    return JsonResponse({"error": "Invalid request"}, status=400)


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


def get_movement_log(request, pk):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Get the instance of the model
    instance = get_object_or_404(Movementg, pk=pk)

    # Filter logs for the specific instance
    logs = LogEntry.objects.filter(
        object_id=instance.pk, content_type__model="movementg"
    )

    def resolve_rig_names(changes):
        """Replace rig IDs with rig names in the changes dict."""
        if "rig" in changes:
            rig_ids = changes["rig"]
            rigs = Rigg.objects.filter(id__in=rig_ids)
            rig_names = [
                rig.Rig_name for rig in rigs
            ]  # Assuming Rig has a 'name' field
            changes["rig"] = rig_names
        return changes

    # Prepare the response data
    log_data = [
        {
            "actor": log.actor.username
            if log.actor
            else "System",  # Use username or handle None
            "object": log.object_repr,
            "changes": resolve_rig_names(
                log.changes_dict
            ),  # Resolve rig names for changes
            "action_time": log.timestamp.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Format the timestamp
        }
        for log in logs
    ]

    # Return the logs as a JSON response (safe=False to allow lists)
    return JsonResponse(log_data, safe=False)


def serialize_related_object(obj):
    """Helper function to serialize a related object if it exists."""
    if obj:
        data = model_to_dict(obj)

        # Handle FieldFile fields by converting them to their URL or path
        for field, value in data.items():
            if isinstance(value, FieldFile):
                data[field] = value.url if value and hasattr(value, "url") else None

        return data
    return None


def get_movementg(request, well_name):
    # Get the list of Movementg instances associated with the well_name
    instances = get_list_or_404(
        Movementg, Well_Construction_Infotion__well_construction_name=well_name
    )

    # Serialize the instances with sub-model fields expanded
    serialized_instances = []
    for instance in instances:
        serialized_instance = model_to_dict(instance)

        # Serialize related foreign key fields
        serialized_instance["rig"] = serialize_related_object(instance.rig)
        serialized_instance["well"] = serialize_related_object(instance.well)
        serialized_instance["Well_Construction_Infotion"] = serialize_related_object(
            instance.Well_Construction_Infotion
        )
        serialized_instance["Cellar"] = serialize_related_object(instance.Cellar)
        serialized_instance["Units"] = serialize_related_object(instance.Units)
        serialized_instance["Eng"] = serialize_related_object(instance.Eng)
        serialized_instance["Contractor"] = serialize_related_object(
            instance.Contractor
        )
        serialized_instance["Construction_Departmeent"] = serialize_related_object(
            instance.Construction_Departmeent
        )
        serialized_instance["HDPE_Installation"] = serialize_related_object(
            instance.HDPE_Installation
        )
        serialized_instance["Pre_Construction"] = serialize_related_object(
            instance.Pre_Construction
        )
        serialized_instance["Rig_Move"] = serialize_related_object(instance.Rig_Move)

        # Append the serialized instance to the list
        serialized_instances.append(serialized_instance)

    # Return the list of serialized instances as JSON
    return JsonResponse(serialized_instances, safe=False)


def Get_Repair_Section(request, pk):
    # Fetch the RepairSection object using the primary key (pk)
    Repair_Section_info = get_object_or_404(RepairSection, pk=pk)

    # Return the required information in a JSON response
    return JsonResponse(
        {
            "REQ_Repair_NUMBER": Repair_Section_info.REQ_Repair_NUMBER,
            "REQ_Repair_Status": Repair_Section_info.REQ_Repair_Status,
            "REQ_Repair_Date": Repair_Section_info.REQ_Repair_Date,
            "Contractor_Contractor_Repair": Repair_Section_info.Contractor_Contractor_Repair,
            "Repair_Start_Date": Repair_Section_info.Repair_Start_Date,
            "Repair_status": Repair_Section_info.Repair_status,
            "Repair_completion_Date": Repair_Section_info.Repair_completion_Date,
            "monitored_By_Repair": Repair_Section_info.monitored_By_Repair,
            "Quantities_Details_Repair": Repair_Section_info.Quantities_Details_Repair,
            "Project_team_Details_Repair": Repair_Section_info.Project_team_Details_Repair,
            "sand_removal": Repair_Section_info.sand_removal,
            "Extension": Repair_Section_info.Extension,
            "Re_Compaction": Repair_Section_info.Re_Compaction,
            "Change_Cellar": Repair_Section_info.Change_Cellar,
            "Modification": Repair_Section_info.Modification,
            "Complete_Repair": Repair_Section_info.Complete_Repair,
            "Additional": Repair_Section_info.Additional,
        }
    )


def Get_Clean_Up_Section(request, pk):
    # Fetch the RepairSection object using the primary key (pk)
    Clean_Up_Section_info = get_object_or_404(Clean_Up_Section, pk=pk)

    # Return the required information in a JSON response
    return JsonResponse(
        {
            "clean_up_request_Number": Clean_Up_Section_info.clean_up_request_Number,
            "clean_up_request_Date": Clean_Up_Section_info.clean_up_request_Date,
            "clean_up_request_Status": Clean_Up_Section_info.clean_up_request_Status,
            "clean_up_construction_contractor": Clean_Up_Section_info.clean_up_construction_contractor,
            "clean_up_KPI": Clean_Up_Section_info.clean_up_KPI,
            "clean_up_start_Date": Clean_Up_Section_info.clean_up_start_Date,
            "clean_Up_start_Status": Clean_Up_Section_info.clean_Up_start_Status,
            "clean_up_completion_date": Clean_Up_Section_info.clean_up_completion_date,
            "clean_up_post_clean_Up_Turnover": Clean_Up_Section_info.clean_up_post_clean_Up_Turnover,
            "clean_up_monitored_by": Clean_Up_Section_info.clean_up_monitored_by,
            "clean_up_Quantities_details": Clean_Up_Section_info.clean_up_Quantities_details,
            "clean_up_project_team_details": Clean_Up_Section_info.clean_up_project_team_details,
            "clean_up_pre_Clean_Up_Turnover": Clean_Up_Section_info.clean_up_pre_Clean_Up_Turnover,
            "clean_up_Criticality": Clean_Up_Section_info.clean_up_Criticality,
        }
    )


def Get_location_Support(request, pk):
    location_Support_info = get_object_or_404(location_Support, pk=pk)
    return JsonResponse(
        {
            "on_location_support_Request_Number": location_Support_info.on_location_support_Request_Number,
            "on_location_support_Request_date": location_Support_info.on_location_support_Request_date,
            "on_location_support_Request_status": location_Support_info.on_location_support_Request_status,
            "on_location_support_contractor": location_Support_info.on_location_support_contractor,
            "on_location_support_dispatch_By": location_Support_info.on_location_support_dispatch_By,
            "on_location_support_Remark": location_Support_info.on_location_support_Remark,
        }
    )
