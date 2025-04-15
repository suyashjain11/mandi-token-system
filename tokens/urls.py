# tokens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_token, name='create_token'),
    path('view/', views.view_token, name='view_token'),
    path('cancel/<int:token_id>/', views.cancel_token, name='cancel_token'),
    path('dashboard/', views.dashboard, name='dashboard'),


]
