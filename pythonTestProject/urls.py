from django.contrib import admin
from django.urls import path
from zipcodes.views import get_location_info
from zipcodes.services import BasicLocationService
from zipcodes.serializers import BasicLocationSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/<str:zip_code>/', lambda request, zip_code: get_location_info(request, zip_code, BasicLocationService(), BasicLocationSerializer), name='get_location_info'),
]