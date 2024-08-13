from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Employee_2(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    supervisor = models.ForeignKey("Supervisor", on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
=======
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d


from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
<<<<<<< HEAD
    # name_to = models.CharField(max_length=200, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)

    # # content_type and object_id should not be nullable if you require them for a valid task
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # assigned_to = GenericForeignKey('content_type', 'object_id')

    # # Allowing assigned_by to be optional
    # assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True, null=True)
    # due_date = models.DateTimeField(blank=True, null=True)
    # start_date = models.DateTimeField(blank=True, null=True)
    # end_date = models.DateTimeField(blank=True, null=True)
    # completed = models.BooleanField(default=False)
    # notes = models.TextField(blank=True, null=True)

    def __str__(self):
        # Improve __str__ to handle the case where both title and name are None
        return self.name or 'Unnamed Task'

    
class GroupWorkshop(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Employee_2)
=======
    name_to = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    assigned_to_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    assigned_to_object_id = models.PositiveIntegerField()
    assigned_to = GenericForeignKey("assigned_to_content_type", "assigned_to_object_id")

    # assigned_to = models.ForeignKey(
    #     "Supervisor", on_delete=models.CASCADE, blank=True, null=True
    # )

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_tasks",
        blank=True,
        null=True,
    )
    due_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Unnamed Task"


class GroupWorkshop(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField("Employee")
>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name
<<<<<<< HEAD
    
=======


>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d
class WellSiteConstruction(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    managers = models.ManyToManyField("Manager", related_name="construction_sites")

    def __str__(self):
        return self.name


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    construction_unit = models.ForeignKey(
        WellSiteConstruction, on_delete=models.CASCADE, related_name="supervisors"
    )
    Manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name="supervisors"
    )

    def __str__(self):
<<<<<<< HEAD
        return f"{self.user.first_name} {self.user.last_name}"
    
=======
        return self.user.username


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}"
>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d


<<<<<<< HEAD
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

=======
class Employee_2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(
        Supervisor, on_delete=models.CASCADE, related_name="employees"
    )
>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d

