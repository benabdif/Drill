
# tasks/forms.py
from django import forms
from .models import Task, GroupWorkshop

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'assigned_by', 'due_date', 'completed', 'notes']


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'assigned_to', 'assigned_by', 'due_date', 'completed', 'notes']

#         widgets = {
#             'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }




class GroupWorkshopForm(forms.ModelForm):
    class Meta:
        model = GroupWorkshop
        fields = ['name', 'members', 'tasks']




