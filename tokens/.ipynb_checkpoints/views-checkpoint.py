from django.shortcuts import render, redirect

# Create your views here.

from .forms import FarmerForm, TokenForm
from .models import Farmer, Token
from datetime import datetime

def create_token(request):
    if request.method == 'POST':
        farmer_form = FarmerForm(request.POST)
        token_form = TokenForm(request.POST)

        if farmer_form.is_valid() and token_form.is_valid():
            farmer = farmer_form.save()
            token = token_form.save(commit=False)
            token.farmer = farmer
            token.token_status = 'active'
            token.save()
            return render(request, 'token_success.html', {'token': token})

    else:
        farmer_form = FarmerForm()
        token_form = TokenForm()

    return render(request, 'create_token.html', {
        'farmer_form': farmer_form,
        'token_form': token_form
    })
