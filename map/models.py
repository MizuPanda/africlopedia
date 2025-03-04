from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, unique=True)  # Two-letter country code
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()
    area = models.FloatField()  # Area in square km

    def __str__(self):
        return f"{self.name} ({self.code})"
