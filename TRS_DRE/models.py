from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.age})"


class Units(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, blank=True)
    name_unit = models.CharField(max_length=100)
    Unit_supervision = models.CharField(max_length=100, null=True, blank=True)
    # rig = models.ForeignKey(Rigg, on_delete=models.SET_NULL, null=True, blank=True, related_name='units')

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
    # location =

    def __str__(self):
        return self.name


class Movementg(models.Model):
    rig = models.ForeignKey(Rigg, on_delete=models.CASCADE)
    well = models.ForeignKey(Wellg, on_delete=models.CASCADE)
    Units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)
    Eng = models.ForeignKey(Engineering, on_delete=models.CASCADE, null=True, blank=True)
    
    Contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField()
    is_cleaned_up = models.BooleanField(default=False)

    def __str__(self):
        # return f"{self.rig.name} from {self.start_date} to {self.end_date}"
        return f"{self.rig.name}"


