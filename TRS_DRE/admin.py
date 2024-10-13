from django.contrib import admin
# from .models import Rig, Engineer

# # Register your models here.
# admin.site.register(Rig)
# admin.site.register(Engineer)

from .models import (
    Rigg,
    Wellg,
    Movementg,
    Units,
    Contractor,
    Engineering,
    Well_Construction_Info,
    Construction_Departmeent,
    Pre_Construction,
    Cellar,
    HDPE_Installation,
    Rig_Move,
    RepairSection,
    RepairSection,
    Clean_Up_Section,
    location_Support,
    
    )

admin.site.register(Rigg)
admin.site.register(Wellg)
admin.site.register(Movementg)
admin.site.register(Units)
admin.site.register(Contractor)
admin.site.register(Engineering)
admin.site.register(Well_Construction_Info)
admin.site.register(Construction_Departmeent)
admin.site.register(Pre_Construction)
admin.site.register(Cellar)
admin.site.register(HDPE_Installation)
admin.site.register(Rig_Move)
admin.site.register(RepairSection)

admin.site.register(Clean_Up_Section)
admin.site.register(location_Support)



