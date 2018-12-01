import uuid

from django.db import models
from django.utils import timezone


def unique_file_path(instance, filename):
    new_file_name = uuid.uuid4()
    return str(new_file_name)

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

class FileModel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    log_file = models.FileField(upload_to=unique_file_path)
    date_processed = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name