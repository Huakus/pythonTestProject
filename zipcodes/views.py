from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
import requests
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_location_info(request, zip_code):
    try:
        url = f'https://www.zipcodeapi.com/rest/{settings.ZIPCODE_API_KEY}/info.json/{zip_code}/degrees'
        response = requests.get(url)

        zip_code_info = response.json()

        location_info = {
            "zip_code": zip_code_info['zip_code'],
            "name": zip_code_info['city'],
            "lat": zip_code_info['lat'],
            "lon": zip_code_info['lng'],
            "state": zip_code_info['state']
        }

        location_serializer = LocationSerializer(data=location_info)
        if location_serializer.is_valid():
            location_serializer.save()
        else:
            logging.warn("location_serializer is not valid for %s", location_info)
        
        return Response(location_info)
    except Exception as e:
        logger.error('Exception getting location info: %s', str(e), exc_info=1)
        raise Http404