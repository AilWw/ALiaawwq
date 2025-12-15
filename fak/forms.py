from django import forms
from .models import FakEntry

class FakEntryForm(forms.ModelForm):
    class Meta:
        model = FakEntry
        fields = ['name', 'identity', 'payment_status', 'whatsapp_name']

