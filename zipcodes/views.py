from django.shortcuts import render
from django.http import Http404
from django.db.models import Model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .services import ILocationService
from .serializers import BasicLocationSerializer
from .models import Location
import logging


logger = logging.getLogger(__name__)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_location_info(request, zip_code, location_service: ILocationService,
                        location_serializer_class: BasicLocationSerializer,
                        location_model_class: Model):
    try:
        try:
            location = location_model_class.objects.get(zip_code=zip_code)
            location_serializer = location_serializer_class(location)
        except location_model_class.DoesNotExist:
            logger.info(f'New Location for zip_code {zip_code}')
            location = location_service.get_location_info(zip_code)
            location_serializer = location_serializer_class(data=location)
            location = location_serializer.validate_and_save()
        return Response(location_serializer.data)
    except Exception as e:
        logger.error('Exception getting location info: %s', str(e), exc_info=1)
        raise Http404
