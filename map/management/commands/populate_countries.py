import requests
from django.core.management.base import BaseCommand
from map.models import Country

class Command(BaseCommand):
    help = "Populate the Country table with selected data from REST Countries API"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data from API"))
            return

        data = response.json()
        countries_added = 0

        for country in data:
            try:
                code = country.get("cca2")  # Two-letter country code
                name = country.get("name", {}).get("common", "")
                official_name = country.get("name", {}).get("official", "")
                capital = country.get("capital", [""])[0]
                population = country.get("population", 0)
                area = country.get("area", 0)
                languages = country.get("languages", {})
                flag_url = country.get("flags", {}).get("svg", "")
                timezone = country.get("timezones", [""])[0]
                gini_index = country.get("gini", {}).get("2018", None)

                # Extract first available currency (default to empty strings if missing)
                currency = next(iter(country.get("currencies", {}).values()), {})
                currency_name = currency.get("name", "")
                currency_symbol = currency.get("symbol", "")

                # Extract English demonyms (default to empty strings if missing)
                demonym_m = country.get("demonyms", {}).get("eng", {}).get("m", "")
                demonym_f = country.get("demonyms", {}).get("eng", {}).get("f", "")

                # Only keep African countries
                if not code or not name or country.get("region") != "Africa":
                    continue  # Skip non-African countries

                # Create or update country record
                obj, created = Country.objects.update_or_create(
                    code=code,
                    defaults={
                        "name": name,
                        "official_name": official_name,
                        "capital": capital,
                        "population": population,
                        "area": area,
                        "languages": languages,
                        "flag_url": flag_url,
                        "timezone": timezone,
                        "gini_index": gini_index,
                        "currency_name": currency_name,
                        "currency_symbol": currency_symbol,
                        "demonym_m": demonym_m,
                        "demonym_f": demonym_f,
                    },
                )

                if created:
                    countries_added += 1

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing {country}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Successfully added/updated {countries_added} countries!"))
