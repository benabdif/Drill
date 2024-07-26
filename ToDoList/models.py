from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    

# class Employee_For_HR(models.Model):
#     name = models.CharField(max_length=200)
#     position = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)

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