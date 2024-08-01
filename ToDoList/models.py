from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class GroupWorkshop(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Employee)
    tasks = models.ManyToManyField(Task)
    def __str__(self):
        return self.name
    


class WellSiteConstruction(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    managers = models.ManyToManyField('Manager', related_name='construction_sites')

    def __str__(self):
        return self.name

class Manager(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    construction_unit = models.ForeignKey(WellSiteConstruction, on_delete=models.CASCADE, related_name='supervisors')
    Manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='supervisors')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Employee_2(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='employees')
    


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
