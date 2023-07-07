import json
import requests

def GetWeather(city):
    # API key for OpenWeatherMap API
    api_key = 'e1ca9fe4899234e124c44c95680caa69'

    # Create the URL for the API request
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Send a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # If the response is successful, parse the JSON data
        data = response.json()
        # print(json.dumps(data, indent=4))

        # Extract the weather data from the JSON response
        weather_data = {
            'city_name': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'visibility': data['visibility'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure']
        }
        return weather_data
    else:
        # If the response is not successful, print an error message
        print('Request failed with status code:', response.status_code)


