from django.db import models
from django.contrib.auth.models import User

class VPNUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    public_key = models.TextField()
    allowed_ips = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class VPNServer(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=100)
    public_key = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.location})"


class VPNConnectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(VPNServer, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} → {self.server.name}"
