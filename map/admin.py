from django.contrib import admin
from .models import Coordinates

# Register your models here.
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ['ip', 'longitude', 'latitude', 'time_logged', 'created', 'updated']
    list_filter = ['longitude', 'latitude']
    search_fields = ['longitude', 'latitude']

admin.site.register(Coordinates, CoordinatesAdmin)
