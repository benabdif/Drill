from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Project,Phase
# Register your models here.

admin.site.register(Project)
admin.site.register(Phase)