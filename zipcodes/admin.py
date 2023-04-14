from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code', 'lat', 'lon', 'state')

admin.site.register(Location, LocationAdmin)