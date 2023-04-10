from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code', 'lat', 'lon', 'state', 'country', 'country_code', 'timestamp')

admin.register(Location, LocationAdmin)