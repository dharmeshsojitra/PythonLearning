import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


city_name = "Mumbai"
pin_code = "400068"
country_code = "US"
API_key = "<Key>"

response= requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}"
                       f"&appid={API_key}&zip={pin_code}")

response_data = json.loads(response.text)

logging.info(f"lat:{response_data['lat']},lon:{response_data['lon']}")

