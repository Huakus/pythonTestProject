from rest_framework import serializers
from .models import Location
import logging

logger = logging.getLogger(__name__)

class BasicLocationSerializer(serializers.Serializer):
    zip_code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6)
    state = serializers.CharField(max_length=100)

    class Meta:
        model = Location
        fields = '__all__'

    def validate_and_save(self):
        if self.is_valid():
            if Location.objects.filter(zip_code=self.data['zip_code']).exists():
                logger.info(f"Location with zip code '{self.data['zip_code']}' already exists.")
                return Location(**self.data)

            location = Location(**self.data)
            location.save()
            return location
        else:
            raise Exception(f"LocationSerializer is not valid for {self.data}")