from django.shortcuts import render, redirect, get_object_or_404
from .forms import FarmerForm
from .models import Farmer, Token, MandiPrice
from datetime import datetime, timedelta, date, time
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.utils.timezone import is_naive,make_aware, now as tz_now, localtime
from reportlab.pdfgen import canvas
from io import BytesIO
import holidays
import pytz

indian_holidays = holidays.India(state='MP')  # Madhya Pradesh Holidays

def home(request):
    return render(request, 'home.html')

from django.utils.timezone import localtime

@login_required
def dashboard(request):
    today = date.today()
    todays_tokens = Token.objects.filter(estimated_arrival_time__date=today).order_by('estimated_arrival_time')
    future_tokens = Token.objects.filter(estimated_arrival_time__date__gt=today).order_by('estimated_arrival_time')
    previous_tokens = Token.objects.filter(estimated_arrival_time__date__lt=today).order_by('-estimated_arrival_time')

    return render(request, 'dashboard.html', {
        'todays_tokens': todays_tokens,
        'future_tokens': future_tokens,
        'previous_tokens': previous_tokens
    })

def create_token(request):
    if request.method == 'POST':
        farmer_form = FarmerForm(request.POST)
        if farmer_form.is_valid():
            farmer = farmer_form.save(commit=False)  # Don't save yet

            crop_type = request.POST.get('crop_type')
            if not crop_type:
                messages.error(request, "Please select a crop type.")
                return render(request, 'create_token.html', {'farmer_form': farmer_form})

            is_tomorrow = request.POST.get('token_date') == 'tomorrow'
            now = localtime()
            target_date = (now + timedelta(days=1)).date() if is_tomorrow else now.date()

            # 🛑 Holiday check
            def is_holiday(d):
                return (
                    d.weekday() == 6 or  # Sunday
                    (d.weekday() == 5 and ((d.day - 1) // 7 + 1 in [2, 4])) or
                    d in indian_holidays
                )

            if is_holiday(target_date):
                messages.error(request, "Mandi is closed on holidays.")
                return render(request, 'create_token.html', {'farmer_form': farmer_form})

            # ⏱️ Delay logic with 15-minute rounding
            if is_tomorrow:
                future_time = make_aware(datetime.combine(target_date, time(8, 0)))
            else:
                future_time = now + timedelta(minutes=30)

            rounded_minute = (future_time.minute // 15 + 1) * 15
            if rounded_minute == 60:
                future_time = future_time.replace(hour=future_time.hour + 1, minute=0, second=0, microsecond=0)
            else:
                future_time = future_time.replace(minute=rounded_minute, second=0, microsecond=0)

            start_time = max(datetime.combine(target_date, time(8, 0), tzinfo=now.tzinfo), now)
            end_time = datetime.combine(target_date, time(19, 0), tzinfo=now.tzinfo)

            next_slot = max(future_time, start_time)
            last_token = Token.objects.filter(estimated_arrival_time__date=target_date).order_by('-estimated_arrival_time').first()
            if last_token:
                candidate_slot = last_token.estimated_arrival_time + timedelta(minutes=15)
                next_slot = max(next_slot, candidate_slot)

            if next_slot > end_time:
                messages.error(request, "All tokens are full for the selected day.")
                return render(request, 'create_token.html', {'farmer_form': farmer_form})

            # Now save farmer and token
            farmer.save()
            token = Token.objects.create(
                farmer=farmer,
                crop_type=crop_type,
                estimated_arrival_time=next_slot,
                token_status='active'
            )

            return render(request, 'token_success.html', {'token': token})

    else:
        farmer_form = FarmerForm()

    return render(request, 'create_token.html', {'farmer_form': farmer_form})


def view_token(request):
    token = None
    not_found = False

    if request.method == 'POST':
        contact = request.POST.get('contact_number')
        farmers = Farmer.objects.filter(contact_number=contact)

        if farmers.exists():
            farmer = farmers.last()
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


def download_token_pdf(request, token_id):
    token = Token.objects.get(id=token_id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, f"Token ID: {token.id}")
    p.drawString(100, 780, f"Farmer Name: {token.farmer.name}")
    p.drawString(100, 760, f"Crop Type: {token.crop_type}")
    p.drawString(100, 740, f"Estimated Arrival Time: {token.estimated_arrival_time}")
    p.drawString(100, 720, f"Status: {token.token_status}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


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
        Token.objects.filter(estimated_arrival_time__date__lt=today).delete()
    return redirect('dashboard')


def mandi_prices_view(request):
    today = date.today()
    today_prices = MandiPrice.objects.filter(date=today).order_by('crop_name')
    return render(request, 'mandi_prices.html', {'prices': today_prices, 'today_date': today})
