from django.urls import path
from .views import country_list

urlpatterns = [
    path("api/countries/", country_list, name="country_list"),
]
