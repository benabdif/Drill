
# tasks/forms.py
from django import forms
from .models import Task, GroupWorkshop

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date', 'completed', 'notes']

class GroupWorkshopForm(forms.ModelForm):
    class Meta:
        model = GroupWorkshop
        fields = ['name', 'members', 'tasks']
