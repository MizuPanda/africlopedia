from django.shortcuts import render
from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all().values("name", "capital", "population", "area", "geojson_data")
    return JsonResponse(list(countries), safe=False)

def map_view(request):
    return render(request, "map/map.html")

def africa_map(request):
    return render(request, "map/africa_map.html")

