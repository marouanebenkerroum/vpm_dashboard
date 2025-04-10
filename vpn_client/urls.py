from django.urls import path
from .views import register_view, login_view, logout_view, request_connection,  server_list, admin_dashboard

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('users/', vpn_users_page, name='vpn_users'),
    path('servers/', server_list, name='server_list'),
    path('servers/request/<int:server_id>/', request_connection, name='request_connection'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),

]
