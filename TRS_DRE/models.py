from django.db import models
from django.core.exceptions import ValidationError


# This is the well information we have
class Well_Construction_Info(models.Model):
    WELL_OBJECTIVE_CHOICES = [
        ('New', 'New'),
        ('Workover', 'Workover'),
    ]
    well_construction_name = models.CharField(max_length=100)
    well_construction_objective = models.CharField(max_length=10,choices=WELL_OBJECTIVE_CHOICES,default='New')
    well_construction_BI = models.IntegerField(blank=True, null=True)
    well_construction_Spud_date = models.DateTimeField(blank=True, null=True)
    well_construction_Reference_Number = models.CharField(max_length=100, null=True, blank=True)
    well_construction_DWO_Engineer = models.CharField(max_length=100, null=True, blank=True)
    well_construction_Producing_Engineer = models.CharField(max_length=100, blank=True, null=True)
    well_construction_Drillsite_Name = models.CharField(max_length=100, null=True, blank=True)
    FLUID_TYPE_CHOICES = [
        ('Oil','Oil'),
        ('Gas','Gas'),
        ('Water','Water'),
    ]
    well_construction_fluid_Type_choices = models.CharField(max_length=10,choices=FLUID_TYPE_CHOICES,default='NA')
    well_construction_Charge_Account = models.IntegerField(blank=True, null=True)
    well_construction_Released_date = models.DateTimeField(blank=True, null=True)
    well_construction_Direct_distance_DH = models.CharField(max_length=100, null=True, blank=True)
    well_construction_Engineering_department = models.CharField(max_length=100, null=True, blank=True)
    well_construction_GOSP_WIP_Department = models.CharField(max_length=100, unique=True, null=True) # I have to ask about that?????? to make sure 


class Units(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, blank=True)
    name_unit = models.CharField(max_length=100)
    Unit_supervision = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_unit


class Contractor (models.Model):
    contractor_ID = models.IntegerField(primary_key=True, null=False, blank=True)
    contractor_name = models.CharField(max_length=100)
    update_L = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.contractor_name


class Engineering (models.Model):
    Eng_ID = models.IntegerField(primary_key=True, null=False, blank=True)
    Eng_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Eng_name




class Rigg(models.Model):
    OIL = "Oil"
    GAS = "Gas"
    WATER = "Water"
    FIELD_TYPE_CHOICES = [
        (OIL, "Oil"),
        (GAS, "Gas"),
        (WATER, "Water"),
    ]
    engineering_name = models.CharField(max_length=100, null=True, blank=True)
    field_type = models.CharField(
        max_length=5, choices=FIELD_TYPE_CHOICES, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    Units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)
    Contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    Eng = models.ForeignKey(Engineering, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Wellg(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)
    progress = models.PositiveIntegerField(default=0, null=True, blank=True)  # Field to store progress percentage


    def __str__(self):
        return self.name


class Movementg(models.Model):
    rig = models.ForeignKey(Rigg, on_delete=models.CASCADE)
    well = models.ForeignKey(Wellg, on_delete=models.CASCADE)
    Units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)
    Eng = models.ForeignKey(Engineering, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    
    Contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_cleaned_up = models.BooleanField(default=False)

    def __str__(self):
        # return f"{self.rig.name} from {self.start_date} to {self.end_date}"
        return f"{self.rig.name}"

    def clean(self):
        # Check for overlapping movements
        overlapping_movements = Movementg.objects.filter(
            rig=self.rig,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(pk=self.pk)

        if overlapping_movements.exists():
            raise ValidationError('A movement already exists for this project within the selected dates.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


#############################



# class RIG_Construction_Info(models.Model):
    






