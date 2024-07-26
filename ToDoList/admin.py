from django.contrib import admin



# Register your models here.

from .models import Employee
from .models import Task
from .models import GroupWorkshop

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(GroupWorkshop)

