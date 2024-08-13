from django.contrib import admin



# Register your models here.

from .models import Employee_2
from .models import Task
from .models import GroupWorkshop
from .models import WellSiteConstruction
from .models import Manager
from .models import Supervisor
from .models import Employee_2


admin.site.register(Employee_2)
admin.site.register(Task)

admin.site.register(GroupWorkshop)
admin.site.register(WellSiteConstruction)
admin.site.register(Manager)
admin.site.register(Supervisor)



