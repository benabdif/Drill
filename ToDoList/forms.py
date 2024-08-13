
# tasks/forms.py
from django import forms
from .models import Task, GroupWorkshop, Supervisor, Employee
from django.contrib.contenttypes.models import ContentType



# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'assigned_by', 'due_date', 'completed', 'notes', 'name_to','start_date', 'end_date'] # , 'assigned_to'



class TaskForm(forms.ModelForm):
    assigned_to_type = forms.ChoiceField(choices=[])
    assigned_to_id = forms.ModelChoiceField(queryset=Supervisor.objects.none())

    class Meta:
        model = Task
<<<<<<< HEAD
        # fields = ['title', 'description', 'assigned_by', 'due_date', 'completed', 'notes', 'name_to','start_date', 'end_date']
        fields = ['title', 'name']
=======
        fields = ['title', 'description', 'assigned_to_type', 'assigned_to_id', 'assigned_by', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        # Set up choices for `assigned_to_type`
        self.fields['assigned_to_type'].choices = [
            (ContentType.objects.get_for_model(Supervisor).id, "Supervisor"),
            (ContentType.objects.get_for_model(Employee).id, "Employee"),
        ]

        # Dynamically update the queryset for `assigned_to_id` based on `assigned_to_type`
        if 'assigned_to_type' in self.data:
            try:
                content_type_id = int(self.data.get('assigned_to_type'))
                model = ContentType.objects.get_for_id(content_type_id).model_class()
                self.fields['assigned_to_id'].queryset = model.objects.all()
            except (ValueError, TypeError):
                pass  # Invalid input from the user, ignore

        elif self.instance.pk:
            # Prepopulate `assigned_to_id` if editing an existing instance
            content_type = self.instance.assigned_to_content_type
            self.fields['assigned_to_type'].initial = content_type.id
            self.fields['assigned_to_id'].queryset = content_type.model_class().objects.all()
            self.fields['assigned_to_id'].initial = self.instance.assigned_to_object_id

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        content_type_id = int(self.cleaned_data['assigned_to_type'])
        task.assigned_to_content_type = ContentType.objects.get_for_id(content_type_id)
        task.assigned_to_object_id = self.cleaned_data['assigned_to_id'].id

        if commit:
            task.save()
        return task
>>>>>>> 5351f0a02930dcef7e245c13f358358ab8cccb8d



class GroupWorkshopForm(forms.ModelForm):
    class Meta:
        model = GroupWorkshop
        fields = ['name', 'members', 'tasks']




