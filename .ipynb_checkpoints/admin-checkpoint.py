from django.contrib import admin

# Register your models here.

from .models import Farmer, Token

admin.site.register(Farmer)
admin.site.register(Token)
