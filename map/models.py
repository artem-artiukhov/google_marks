from django.db import models
from django.utils import timezone

# Create your models here.
class Coordinates(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    time_logged = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip