from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import VPNUser
from .serializers import VPNUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vpn_users')
    else:
        form = RegisterForm()
    return render(request, 'vpn/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('vpn_users')
    else:
        form = AuthenticationForm()
    return render(request, 'vpn/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def vpn_users_page(request):
    users = VPNUser.objects.all()
    return render(request, 'vpn/vpn_users.html', {'users': users})
