from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register_page(request):
    return render(request, 'register.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('dashboard/', dashboard),
    path('register/', register_page),
    path('api/accounts/', include('accounts.urls')),
    path('api/properties/', include('properties.urls')),
    path('api/favourites/', include('favourites.urls')),
]
