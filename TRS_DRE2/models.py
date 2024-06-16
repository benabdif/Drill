from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


class Project(models.Model):
    name = models.CharField(max_length=100)
    well = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
      return self.name
    



# new models:

class RigW(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class WellW(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RigMoveW(models.Model):
    rig = models.ForeignKey(RigW, on_delete=models.CASCADE)
    from_well = models.ForeignKey(WellW, related_name='rig_moves_from', on_delete=models.CASCADE)
    to_well = models.ForeignKey(WellW, related_name='rig_moves_to', on_delete=models.CASCADE)
    move_date = models.DateField()

    def __str__(self):
        return f"{self.rig.name} moved from {self.from_well.name} to {self.to_well.name} on {self.move_date}"
