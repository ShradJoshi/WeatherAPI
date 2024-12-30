import requests
import config


class City:
    def __init__(self, name, lat, lon, units):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.token = config.token

        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={self.token}")
            self.response_json = response.json()
            self.temp = self.response_json["main"]["temp"]
            self.temp_min = self.response_json["main"]["temp_min"]
            self.temp_max = self.response_json["main"]["temp_max"]
        
        except:
            print("No internet access!")


    
    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")

my_city = City ("Kathmandu",27.700769, 85.300140, units ="imperial")
my_city.temp_print()

vacation_city = City ( "Toronto", 43.70643, -79.39864, units = "metric")
vacation_city.temp_print()
print(vacation_city.response_json)

