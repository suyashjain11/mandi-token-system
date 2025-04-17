from django.contrib import admin
from .models import Farmer, Token # type: ignore

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['name', 'village', 'contact_number', 'registration_date']
    search_fields = ['name', 'village', 'contact_number']

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'farmer', 'crop_type', 'estimated_arrival_time', 'token_status', 'redeemed']
    list_filter = ['token_status', 'redeemed']
    search_fields = ['farmer__name', 'crop_type']
