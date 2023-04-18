from django.test import TestCase
from unittest.mock import MagicMock
from django.test import RequestFactory
from .views import get_location_info
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

class GetLocationInfoTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_location_info_ok_from_db(self):
        request = self.factory.get('/api/locations?zip_code=12345')
        user = User.objects.create_user('joaquin', 'joaquin@email.com', '123qwe')
        force_authenticate(request, user=user)
        request.query_params = {'zip_code': '12345'}

        location_service = MagicMock()
        location_model_class = MagicMock()
        location_serializer_class = MagicMock()
        
        location_serializer_class.return_value.data = {
                'zip_code': '12345',
                'city': 'Testville',
                'lat': 123.4,
                'lon': 234.5,
                'state': 'CA'
            }

        response = get_location_info(request, '12345', location_service, location_serializer_class, location_model_class)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
                'zip_code': '12345',
                'city': 'Testville',
                'lat': 123.4,
                'lon': 234.5,
                'state': 'CA'
            })