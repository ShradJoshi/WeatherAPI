import json
from weather import City

my_city = City ("Kathmandu",27.700769, 85.300140, units ="imperial")
my_city.temp_print()

vacation_city = City ( "Toronto", 43.70643, -79.39864, units = "metric")
vacation_city.temp_print()


print(json.dumps(vacation_city.response_json, indent=4))