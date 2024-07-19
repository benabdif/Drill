from django.contrib import admin
# from .models import Rig, Engineer

# # Register your models here.
# admin.site.register(Rig)
# admin.site.register(Engineer)


from .models import Rigg, Wellg, Movementg, Units, Contractor, Engineering

admin.site.register(Rigg)
admin.site.register(Wellg)
admin.site.register(Movementg)
admin.site.register(Units)
admin.site.register(Contractor)
admin.site.register(Engineering)




 