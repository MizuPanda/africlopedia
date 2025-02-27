from django.urls import path
from .views import country_list, map_view, africa_map


urlpatterns = [
    path("api/countries/", country_list, name="country_list"),
    path("", africa_map, name="africa_map"),  
]