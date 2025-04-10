from django.db import models

class VPNUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    public_key = models.TextField()
    allowed_ips = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
