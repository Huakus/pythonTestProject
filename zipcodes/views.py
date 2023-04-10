from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_location_info(request):
    try:
        
        return Response()
    except Exception as e:
        logger.error("Exception getting location info: %s", str(e))
        raise Http404