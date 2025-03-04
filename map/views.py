from django.shortcuts import render
from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all().values("code", "name", "capital", "population", "area")
    return JsonResponse(list(countries), safe=False)

def africa_map(request):
    return render(request, "map/africa_map.html")

