travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(new_country, new_visits, new_cities):
    add_dict = {"country":new_country, "visits":new_visits, "cities":new_cities}
    travel_log.append(add_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)