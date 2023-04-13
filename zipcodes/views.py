from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import ILocationService
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_location_info(request, zip_code, location_service: ILocationService, location_serializer_class):
    try:
        location_info = location_service.get_location_info(zip_code)
        location_serializer = location_serializer_class(data=location_info)

        if location_serializer.is_valid():
            location_serializer.save()
        else:
            logging.warn("location_serializer is not valid for %s", location_info)

        return Response(location_info)
    except Exception as e:
        logger.error('Exception getting location info: %s', str(e), exc_info=1)
        raise Http404
