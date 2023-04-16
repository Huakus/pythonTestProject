from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from zipcodes.views import get_location_info
from zipcodes.services import BasicLocationService
from zipcodes.serializers import BasicLocationSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('location/<str:zip_code>/', lambda request, zip_code: get_location_info(request, zip_code, BasicLocationService(), BasicLocationSerializer), name='get_location_info'),
]