from django.shortcuts import render, redirect, get_object_or_404
from .forms import FarmerForm
from .models import Farmer, Token
from datetime import datetime,timedelta,date
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.utils.timezone import now


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    today = date.today()
    todays_tokens = Token.objects.filter(estimated_arrival_time__date=today).order_by('estimated_arrival_time')
    previous_tokens = Token.objects.exclude(estimated_arrival_time__date=today)
    return render(request, 'dashboard.html', {
        'todays_tokens': todays_tokens,
        'previous_tokens': previous_tokens
    })


def create_token(request):
    if request.method == 'POST':
        farmer_form = FarmerForm(request.POST)
        

        if farmer_form.is_valid():  
            farmer = farmer_form.save()
            
            # Set slot interval (e.g., 15 mins per token)
            interval = timedelta(minutes=15)
            start_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

            # Get the last token issued today
            today_tokens = Token.objects.filter(estimated_arrival_time__date=datetime.today().date()).order_by('-estimated_arrival_time')

            if today_tokens.exists():
                last_slot = today_tokens[0].estimated_arrival_time
                next_slot = last_slot + interval
            else:
                next_slot = start_time

            # Create and save token
            token = Token.objects.create(
                farmer=farmer,
                crop_type=request.POST.get('crop_type'),
                estimated_arrival_time=next_slot,
                token_status='active'
            )

            messages.success(request, "Token created successfully!")

            send_mail(
                subject='Mandi Token Confirmation',
                message=f'Hello {farmer.name}, your token has been generated.\n\nCrop: {token.crop_type}\nArrival Time: {token.estimated_arrival_time.strftime("%I:%M %p")}\n\nPlease be present at the mandi at this time.',
                from_email='no-reply@mandiapp.com',
                recipient_list=['test@example.com'],  # Use actual farmer email when added
                fail_silently=True
)

            return render(request, 'token_success.html', {'token': token})

    else:
        farmer_form = FarmerForm()

    return render(request, 'create_token.html', {
        'farmer_form': farmer_form
    })

def view_token(request):
    token = None
    not_found = False

    if request.method == 'POST':
        contact = request.POST.get('contact_number')

        print(f"Contact entered: {contact}")  # Debug line

        farmers = Farmer.objects.filter(contact_number=contact)

        print(f"Farmers count: {farmers.count()}")  # Debug line
        
        if farmers.exists():
            farmer = farmers.last()  # or .first() 
            tokens = Token.objects.filter(farmer=farmer)
            if tokens.exists():
                token = tokens.latest('estimated_arrival_time')
            else:
                not_found = True
        else:
            not_found = True
    return render(request, 'view_token.html', {
        'token': token,
        'not_found': not_found
    })

def redeem_token(request, token_id):
    token = get_object_or_404(Token, id=token_id)
    token.redeemed = True
    token.save()
    return redirect('dashboard')

def cancel_token(request, token_id):
    token = get_object_or_404(Token, pk=token_id)
    token.token_status = 'cancelled'
    token.save()
    return HttpResponseRedirect(reverse('view_token'))

def delete_old_tokens(request):
    if request.method == "POST":
        today = date.today()
        Token.objects.exclude(estimated_arrival_time__date=today).delete()
    return redirect('dashboard')
