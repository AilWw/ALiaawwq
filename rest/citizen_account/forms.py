from django import forms
from .models import CitizenAccountEntry

class CitizenAccountEntryForm(forms.ModelForm):
    class Meta:
        model = CitizenAccountEntry
        fields = ['name', 'identity']

