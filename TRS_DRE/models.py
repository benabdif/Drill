from django.db import models
from django.core.exceptions import ValidationError
from auditlog.registry import auditlog


#  Well_Construction_Infotion
# This is the well information we have (1)
class Well_Construction_Info(models.Model):
    WELL_OBJECTIVE_CHOICES = [
        ("New", "New"),
        ("Workover", "Workover"),
    ]
    well_construction_name = models.CharField(max_length=100)
    well_construction_objective = models.CharField(
        max_length=10, choices=WELL_OBJECTIVE_CHOICES, default="New"
    )
    well_construction_BI = models.IntegerField(blank=True, null=True)
    well_construction_Spud_date = models.DateTimeField(blank=True, null=True)
    well_construction_Reference_Number = models.CharField(
        max_length=100, null=True, blank=True
    )
    well_construction_DWO_Engineer = models.CharField(
        max_length=100, null=True, blank=True
    )
    well_construction_Producing_Engineer = models.CharField(
        max_length=100, blank=True, null=True
    )
    well_construction_Drillsite_Name = models.CharField(
        max_length=100, null=True, blank=True
    )
    FLUID_TYPE_CHOICES = [
        ("Oil", "Oil"),
        ("Gas", "Gas"),
        ("Water", "Water"),
    ]
    well_construction_fluid_Type_choices = models.CharField(
        max_length=10, choices=FLUID_TYPE_CHOICES, default="NA"
    )
    well_construction_Charge_Account = models.IntegerField(blank=True, null=True)
    well_construction_Released_date = models.DateTimeField(blank=True, null=True)
    well_construction_Direct_distance_DH = models.CharField(
        max_length=100, null=True, blank=True
    )
    well_construction_Engineering_department = models.CharField(
        max_length=100, null=True, blank=True
    )
    well_construction_GOSP_WIP_Department = models.CharField(
        max_length=100, unique=True, null=True
    )  # I have to ask about that?????? to make sure

    
    def __str__(self):
        return f"{self.well_construction_name} (ID : {self.id})"


# This is Construction Information (2)


class Construction_Departmeent(models.Model):
    CONSTR_REQ = models.IntegerField(
        null=True, blank=True
    )  # we havr to thank about this if this should be
    REQ_Start_Date = models.DateField(null=True, blank=True)
    REQ_Status = models.CharField(max_length=100, null=True, blank=True)
    CONSTR_Contractor = models.CharField(max_length=100, null=True, blank=True)

    CONSTR_KPI = models.IntegerField(null=True, blank=True)
    CONSTR_KOM = models.DateField(null=True, blank=True)
    Conducted_by_KOM = models.CharField(max_length=100, null=True, blank=True)
    Construction_Status = models.IntegerField(null=True, blank=True)

    CONSTR_Skid_ROAD_DIST = models.IntegerField(null=True, blank=True)
    Final_Survey = models.CharField(max_length=100, null=True, blank=True)
    Conducted_by_Final_Survey = models.CharField(max_length=100, null=True, blank=True)
    Unit = models.CharField(max_length=100, null=True, blank=True)

    Post_CONSTR_Rurn_OVER = models.CharField(max_length=100, null=True, blank=True)
    REQ_End_Date = models.DateField(null=True, blank=True)
    Quanatities_Detities = models.CharField(max_length=100, null=True, blank=True)
    Project_team_Details = models.CharField(max_length=100, null=True, blank=True)

    Remark_and_Hold = models.CharField(max_length=100, null=True, blank=True)
    YES_NO_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]
    Criticality = models.CharField(
        max_length=3, choices=YES_NO_CHOICES, default="Yes/No"
    )


# This is the Pre_construction Table (3)
class Pre_Construction(models.Model):
    Approval_Status = models.CharField(max_length=100, null=True, blank=True)
    RQE_CHOICES = [
        ("Strip", "Strip"),
        ("Logistic", "Logistic"),
        ("Access", "Access"),
    ]
    CONDTR_REQ = models.CharField(
        max_length=100, null=True, blank=True, choices=RQE_CHOICES
    )
    Approved_Lay_out = models.CharField(max_length=100, null=True, blank=True)
    Date_Approved_Lay_out = models.DateField(null=True, blank=True)

    Approval_Date = models.DateField(null=True, blank=True)
    R_Completio_Date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"ID #: {self.id}"

    
    


# This is the Cellar Table (4)
class Cellar(models.Model):
    Cellar_Installation = models.CharField(max_length=100, null=True, blank=True)
    Soil_Test_Request = models.IntegerField(null=True, blank=True)
    REQ_Date = models.DateField(null=True, blank=True)
    Cellar_REQ_Status = models.CharField(max_length=100, null=True, blank=True)
    Soil_Test_Contractor = models.CharField(max_length=100, null=True, blank=True)
    Conducted_by = models.CharField(max_length=100, null=True, blank=True)


# This is the HDPE Installation (5)
class HDPE_Installation(models.Model):
    Lining_Installation = models.CharField(max_length=100, null=True, blank=True)
    REQ_Lining_Number = models.IntegerField(null=True, blank=True)
    HDPE_REQ_Date = models.DateField(null=True, blank=True)
    HDPE_REQ_Status = models.CharField(max_length=100, null=True, blank=True)

    Installation_Status = models.CharField(max_length=100, null=True, blank=True)
    Total_Area_Installed = models.IntegerField(null=True, blank=True)
    Lining_Contractor = models.CharField(max_length=100, null=True, blank=True)
    Conducted_by_info = models.CharField(max_length=100, null=True, blank=True)
    Quantities_Details = models.CharField(max_length=10, null=True, blank=True)


# I have to create more than one model( 1- Rig_move 2- Repair-Section 3- Clean-Up Section 4- on location Support Waste Manament 5- Change Request Track )


# Rig_move
class Rig_Move(models.Model):
    RIG_MOVE_REQ = models.IntegerField(null=True, blank=True)
    RIG_MOVE_NAME = models.CharField(max_length=100, null=True, blank=True)
    RIG_MOVE_WELL = models.CharField(max_length=100, null=True, blank=True)
    RIG_MOVE_STATUS = models.CharField(max_length=100, null=True, blank=True)
    RIG_MOVE_DOCUMENTS = models.FileField(
        upload_to="rig_move_documents/", null=True, blank=True
    )
    RIG_MOVE_CONDUCTED_BY = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.RIG_MOVE_NAME

class RepairSection(models.Model):
    sand_removal = models.BooleanField(default=False, blank=True)
    Extension = models.BooleanField(default=False, blank=True)
    Re_Compaction = models.BooleanField(default=False, blank=True)
    Change_Cellar = models.BooleanField(default=False, blank=True)
    Modification = models.BooleanField(default=False, blank=True)
    Complete_Repair = models.BooleanField(default=False, blank=True)
    Additional = models.BooleanField(default=False, blank=True)
    REQ_Repair_NUMBER = models.IntegerField(null=True, blank=True)
    REQ_Repair_Status = models.CharField(max_length=100, null=True, blank=True)
    REQ_Repair_Date = models.DateField(null=True, blank=True)
    Contractor_Contractor_Repair = models.CharField(null=True, blank=True)
    Repair_Start_Date = models.CharField(null=True, blank=True)

    Repair_Start_date = models.DateField(null=True, blank=True)
    Repair_status = models.CharField(max_length=100, null=True, blank=True)
    Repair_completion_Date = models.DateField(null=True, blank=True)
    monitored_By_Repair = models.CharField(max_length=100, null=True, blank=True)
    Quantities_Details_Repair = models.CharField(max_length=100, null=True, blank=True)
    Project_team_Details_Repair = models.CharField(
        max_length=100, null=True, blank=True
    )

    FLUID_TYPE_CHOICES = [("Yes", "No")]
    Repair_Criticality = models.CharField(
        max_length=10, choices=FLUID_TYPE_CHOICES, default="N/A"
    )


# This is for the clean up table models 
class Clean_Up_Section(models.Model):
    clean_up_request_Number = models.IntegerField(null=True, blank=True)
    clean_up_request_Date = models.DateField(null=True, blank=True)
    clean_up_request_Status = models.CharField(max_length=100, null=True, blank=True)
    clean_up_construction_contractor = models.CharField(max_length=100, null=True, blank=True)
    clean_up_KPI = models.IntegerField(null=True, blank=True)
    clean_up_start_Date = models.DateField(null=True, blank=True) 
    clean_Up_start_Status = models.CharField(max_length=100, null=True, blank=True)
    clean_up_completion_date = models.DateField(null=True, blank=True)
    clean_up_post_clean_Up_Turnover = models.CharField(max_length=100, null=True, blank=True)
    clean_up_monitored_by = models.CharField(max_length=100, null=True, blank=True)
    clean_up_Quantities_details = models.CharField(max_length=200, null=True, blank=True)
    clean_up_project_team_details = models.CharField(max_length=200, null=True, blank=True)
    clean_up_pre_Clean_Up_Turnover = models.CharField(max_length=100, null=True, blank=True)
    FLUID_TYPE_CHOICES_CRITICALITY = [
        ('YES','YES'),
        ('No','No'),
    ]
    clean_up_Criticality = models.CharField(max_length=10, choices=FLUID_TYPE_CHOICES_CRITICALITY, default='N/A')

    def __str__(self):
        return self.clean_up_construction_contractor

# This is the new modle we
class location_Support(models.Model):
    on_location_support_Request_Number = models.IntegerField(null=True, blank=True)
    on_location_support_Request_date = models.DateField(null=True, blank=True)
    on_location_support_Request_status = models.CharField(max_length=100, null=True, blank=True)
    on_location_support_contractor = models.CharField(max_length=100, null=True, blank=True)
    on_location_support_dispatch_By = models.CharField(max_length=100, null=True, blank=True)
    on_location_support_Remark = models.CharField(max_length=100, null=True, blank=True)












class Units(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, blank=True)
    name_unit = models.CharField(max_length=100)
    Unit_supervision = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_unit


class Contractor(models.Model):
    contractor_ID = models.IntegerField(primary_key=True, null=False, blank=True)
    contractor_name = models.CharField(max_length=100)
    update_L = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.contractor_name


class Engineering(models.Model):
    Eng_ID = models.IntegerField(primary_key=True, null=False, blank=True)
    Eng_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Eng_name


class Rigg(models.Model):
    Rig_name = models.CharField(max_length=100)
    Exp = "Exp"
    Gas_Dev = "Gas Dev..."
    UR = "UR"
    FIELD_TYPE_CHOICES = [
        (Exp, "Exp"),
        (Gas_Dev, "Gas Dev..."),
        (UR, "UR"),
    ]
    Rig_Type = models.CharField(
        max_length=100, choices=FIELD_TYPE_CHOICES, null=True, blank=True
    )
    Operation_Department = models.CharField(max_length=100, null=True, blank=True)
    Operation_Manager = models.CharField(max_length=100, null=True, blank=True)
    Permanent_Construction_Cc = models.CharField(max_length=100, null=True, blank=True)
    Last_Update_Permanent_Construction_Cc = models.DateField(null=True, blank=True)
    Permanent_HDPE_Contractor = models.CharField(max_length=100, null=True, blank=True)
    Last_Update_Permanent_HDPE_Contractor = models.DateField(null=True, blank=True)
    Permanent_Soil_Test_Contractor = models.CharField(
        max_length=100, null=True, blank=True
    )
    Last_Update_Permanent_Soil_Test_Contractor = models.DateField(null=True, blank=True)
    Current_Assigned_Unit = models.CharField(max_length=100, null=True, blank=True)
    Current_Assigned_WS_Engineer = models.CharField(
        max_length=100, null=True, blank=True
    )

    # Units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)
    # Contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    # Eng = models.ForeignKey(Engineering, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.Rig_name

# We have to cancel this models
class Wellg(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)
    progress = models.PositiveIntegerField(
        default=0, null=True, blank=True
    )  # Field to store progress percentage

    def __str__(self):
        return self.name


# This is for the Movementg
class Movementg(models.Model):
    rig = models.ForeignKey(Rigg, on_delete=models.CASCADE)
    well = models.ForeignKey(Wellg, on_delete=models.CASCADE)
    Well_Construction_Infotion = models.ForeignKey(
        Well_Construction_Info, on_delete=models.CASCADE, null=True, blank=True
    )
    Cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, null=True, blank=True)
    Units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)
    Eng = models.ForeignKey(
        Engineering, on_delete=models.CASCADE, null=True, blank=True
    )
    note = models.TextField(null=True, blank=True)
    Contractor = models.ForeignKey(
        Contractor, on_delete=models.CASCADE, null=True, blank=True
    )
    Construction_Departmeent = models.ForeignKey(
        Construction_Departmeent, on_delete=models.CASCADE, null=True, blank=True
    )
    HDPE_Installation = models.ForeignKey(
        HDPE_Installation, on_delete=models.CASCADE, null=True, blank=True
    )
    Pre_Construction = models.ForeignKey(
        Pre_Construction, on_delete=models.CASCADE, null=True, blank=True
    )
    Rig_Move = models.ForeignKey(
        Rig_Move, on_delete=models.CASCADE, null=True, blank=True
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_cleaned_up = models.BooleanField(default=False)

    def __str__(self):
        # return f"{self.rig.name} from {self.start_date} to {self.end_date}"
        return f"{self.rig}"

    def clean(self):
        # Check for overlapping movements
        overlapping_movements = Movementg.objects.filter(
            rig=self.rig, start_date__lt=self.end_date, end_date__gt=self.start_date
        ).exclude(pk=self.pk)

        if overlapping_movements.exists():
            raise ValidationError(
                "A movement already exists for this project within the selected dates."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


auditlog.register(Movementg)    