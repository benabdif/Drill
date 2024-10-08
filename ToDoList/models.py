from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Employee_2(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    supervisor = models.ForeignKey("Supervisor", on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    # name_to = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)



    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        # Improve __str__ to handle the case where both title and name are None
        return self.name or 'Unnamed Task'

    
class GroupWorkshop(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Employee_2)
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
    

    

# class Employee_2(models.Model):
#     user = models.OneToOneField(User,  on_delete=models.CASCADE)
#     supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='employees')

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"



# from django.db import models
# from django.contrib.auth.models import User

# class Manager(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"



# class superv(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"


