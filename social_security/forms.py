from django import forms
from .models import SocialSecurityEntry

class SocialSecurityEntryForm(forms.ModelForm):
    class Meta:
        model = SocialSecurityEntry
        fields = ['name', 'identity']

