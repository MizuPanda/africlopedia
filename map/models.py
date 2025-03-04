from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, unique=True)  # cca2
    name = models.CharField(max_length=100, unique=True)  # name.common
    official_name = models.CharField(max_length=200)  # name.official
    capital = models.CharField(max_length=100, blank=True)  # capital[0]
    population = models.BigIntegerField()
    area = models.FloatField()  # Area in km²
    languages = models.JSONField(default=dict)  # Stores languages as a JSON object
    flag_url = models.URLField()  # flags.svg
    timezone = models.CharField(max_length=50)  # timezones[0]
    currency_name = models.CharField(max_length=100, blank=True)  # currencies.NGN.name
    currency_symbol = models.CharField(max_length=10, blank=True)  # currencies.NGN.symbol
    demonym_m = models.CharField(max_length=100, blank=True)  # demonyms.eng.m
    demonym_f = models.CharField(max_length=100, blank=True)  # demonyms.eng.f

    def __str__(self):
        return f"{self.name} ({self.code})"