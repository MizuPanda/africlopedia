from django.shortcuts import render
from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all().values("name", "capital", "population", "area", "geojson_data")
    return JsonResponse(list(countries), safe=False)
