from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()
    area = models.FloatField()  # Area in square km
    geojson_data = models.JSONField()  # Store map data as GeoJSON

    def __str__(self):
        return self.name
