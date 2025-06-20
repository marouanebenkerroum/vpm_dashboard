from django import forms
from django.forms import CharField, ModelForm, PasswordInput
from .models import Firewall

class FirewallForm(ModelForm):
    firewall_pass = CharField(widget=forms.PasswordInput)
    class Meta:
        model = Firewall
        fields = ['firewall_pass']
