from __future__ import unicode_literals
from django.db import models
from django.forms import CharField

class Datacenter(models.Model):
    datacenter_code = models.CharField('Datacenter Code', max_length=10)
    datacenter_active = models.BooleanField('Datacenter Active?', default=True)
    def __str__(self):
        return self.datacenter_code

class firewall(models.Model):
    firewall_name = models.CharField('Firewall Name', max_length=50)
    firewall_location = models.ForeignKey('Datacenter', on_delete=models.CASCADE)
    firewall_active = models.BooleanField('Firewall Active?', default=True)
    firewall_manageip = models.GenericIPAddressField('Management IP')
    firewall_vpnip = models.GenericIPAddressField('VPN Interface IP')
    firewall_user = models.CharField('API User', max_length=50, blank=True)
    firewall_pass = models.CharField('API Pass', max_length=50, blank=True)
    firewall_vpnstatus = models.TextField(editable=False, blank=True)
    def __str__(self):
        return self.firewall_name
# Create your models here.
