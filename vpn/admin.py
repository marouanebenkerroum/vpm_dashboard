
from django.contrib import admin
from .models import firewall, Datacenter

class FirewallAdmin(admin.ModelAdmin):
    list_display = ('firewall_name', 'firewall_location', 'firewall_active', 'firewall_manageip', 'firewall_vpnip', 'firewall_user')  # Customize columns you want to display
    search_fields = ('firewall_name', 'firewall_user')  # Add fields you want to search by

admin.site.register(firewall, FirewallAdmin)

class DatacenterAdmin(admin.ModelAdmin):
    list_display = ('datacenter_code', 'datacenter_active')

admin.site.register(Datacenter,DatacenterAdmin)

