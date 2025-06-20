from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import VPNUser, VPNConnectionRequest, VPNServer
from .serializers import VPNUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('server_list')
    else:
        form = RegisterForm()
    return render(request, 'vpn/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('server_list')
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

@login_required
def server_list(request):
    servers = VPNServer.objects.all()
    return render(request, 'vpn/server_list.html', {'servers': servers})



@login_required
def request_connection(request, server_id):
    server = get_object_or_404(VPNServer, id=server_id)
    VPNConnectionRequest.objects.create(user=request.user, server=server)
    messages.success(request, f"You are now connected to {server.name}.")
    return redirect('server_list')


@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    servers = VPNServer.objects.all()
    data = []
    for server in servers:
        connections = VPNConnectionRequest.objects.filter(server=server)
        data.append((server, connections))
    return render(request, 'vpn/admin_dashboard.html', {'data': data})
