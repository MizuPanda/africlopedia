import json
from map.models import Country

# Load country data from a JSON file
with open("africa_countries.json", "r") as file:
    data = json.load(file)

for country in data:
    Country.objects.update_or_create(
        name=country["name"],
        defaults={
            "capital": country["capital"],
            "population": country["population"],
            "area": country["area"],
            "geojson_data": country["geojson"],
        }
    )

print("✅ Country data successfully loaded!")
