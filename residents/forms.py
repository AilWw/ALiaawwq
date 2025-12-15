from django import forms
from .models import ResidentEntry

class ResidentEntryForm(forms.ModelForm):
    class Meta:
        model = ResidentEntry
        fields = ['name', 'residency_number', 'company', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

