from django import forms
from .models import eHighlight_Record

class eHighlightRecordForm(forms.ModelForm):
    class Meta:
        model = eHighlight_Record
        fields = ['date', 'week', 'Cost', 'unit', 'highlight_type', 'wellsite_activity', 'details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
            
        }


# from django import forms
# from .models import eHighlight_Record

# class eHighlightRecordForm(forms.ModelForm):
#     class Meta:
#         model = eHighlight_Record
#         exclude = ['date']  # Exclude the non-editable date field
