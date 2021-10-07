import requests
from pprint import pprint

API_Key = 'a77d62e9c449509c177e8d07aacc9ff7'

city = input('Enter a city: ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)
