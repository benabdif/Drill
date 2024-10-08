
# tasks/forms.py
from django import forms
from .models import Task, GroupWorkshop



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ['title', 'description', 'assigned_by', 'due_date', 'completed', 'notes', 'name_to','start_date', 'end_date']
        fields = ['title', 'name', 'start_date', 'end_date','description', 'assigned_to','assigned_by']



class GroupWorkshopForm(forms.ModelForm):
    class Meta:
        model = GroupWorkshop
        fields = ['name', 'members', 'tasks']




