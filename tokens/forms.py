from django import forms
from .models import Farmer, Token

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'village', 'contact_number']

