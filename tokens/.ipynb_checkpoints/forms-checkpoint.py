from django import forms
from .models import Farmer, Token

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'village', 'contact_number']

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['crop_type', 'estimated_arrival_time']
