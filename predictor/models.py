
from django.db import models

class PredictionLog(models.Model):
    input_data = models.TextField()
    prediction = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)