from django.contrib import admin
from .models import Member, Project, RigW,WellW,RigMoveW
# Register your models here.

admin.site.register(Member)
admin.site.register(Project)
admin.site.register(RigW)
admin.site.register(WellW)
admin.site.register(RigMoveW)
