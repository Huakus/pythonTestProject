from django.db import models

class Location(models.Model):
    zip_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=5)