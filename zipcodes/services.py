import requests
from django.conf import settings
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class ILocationService:
    def get_location_info(self, zip_code: str) -> dict:
        pass

    def validate_response(self, url:str, response:Response):
        if response.status_code != 200:
            raise Exception(f"Error code {response.status_code} trying to get location information from {url}: {response.json()}")


class BasicLocationService(ILocationService):
    def get_location_info(self, zip_code):
        url = f'https://www.zipcodeapi.com/rest/{settings.ZIPCODE_API_KEY}/info.json/{zip_code}/degrees'
        
        response = requests.get(url)

        super().validate_response(url, response)

        zip_code_info = response.json()

        location_info = {
            "zip_code": zip_code_info['zip_code'],
            "name": zip_code_info['city'],
            "lat": zip_code_info['lat'],
            "lon": zip_code_info['lng'],
            "state": zip_code_info['state']
        }

        return location_info