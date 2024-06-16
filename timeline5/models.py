from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phase(models.Model):
    project = models.ForeignKey(Project, related_name='phases', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_month = models.IntegerField(choices=[(i, month) for i, month in enumerate(
        ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"], 1)])
    end_month = models.IntegerField(choices=[(i, month) for i, month in enumerate(
        ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"], 1)])
    
    # years = models.IntegerField(choices=[(i, month) for i, month in enumerate(
    #     ["2024", "2025", "2026", "2027", "2028", "2029","2030"], 1)])

    def __str__(self):
        return f"{self.name} ({self.start_month}-{self.end_month})"
