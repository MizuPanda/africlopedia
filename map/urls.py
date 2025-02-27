from django.urls import path
from .views import country_list, map_view

urlpatterns = [
    path("api/countries/", country_list, name="country_list"),
    path("", map_view, name="map_view"),
]
