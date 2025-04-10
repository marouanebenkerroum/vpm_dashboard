from rest_framework import serializers
from .models import VPNUser

class VPNUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPNUser
        fields = '__all__'
