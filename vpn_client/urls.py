from django.urls import path
from .views import register_view, login_view, logout_view, vpn_users_page

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', vpn_users_page, name='vpn_users'),
]
