from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import ILocationService
from .models import Location
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_location_info(request, zip_code, location_service: ILocationService, location_serializer_class):
    try:
        try:
            location = Location.objects.get(zip_code=zip_code)

        except Location.DoesNotExist:
            logger.info(f"New Location for zip_code {zip_code}")
            location = location_service.get_location_info(zip_code)
            location_serializer = location_serializer_class(data=location)
            location = location_serializer.validate_and_save()

        location_serializer = location_serializer_class(location)
        return Response(location_serializer.data)
    except Exception as e:
        logger.error('Exception getting location info: %s', str(e), exc_info=1)
        raise Http404
