from pages.drivers import Drivers
from pages.weather_page import WeatherPage
from get_data_api import GetWeather
import re

def verify_city_name(api_city_name, web_city_name):
    assert api_city_name == web_city_name, f'API city: {api_city_name} differ web city: {web_city_name}'

def verify_temperature_value(api_temperature, web_temperature, tolerance):
    assert abs(api_temperature - web_temperature) <= tolerance, \
        f'API temperature: {api_temperature} differs Web temperature: {web_temperature}'

def verify_feels_like_value(api_feels_like, web_feels_like, tolerance):
    assert abs(api_feels_like - web_feels_like) <= tolerance, \
        f'API feels like: {api_feels_like} differs Web feels like: {web_feels_like}'

def verify_humidity_value(api_humidity, web_humidity):
    assert api_humidity == web_humidity, \
        f'api humidity: {api_humidity} differs web humidity: {web_humidity}'

def verify_visibility_value(api_visibility, web_visibility):
    assert api_visibility == web_visibility * 1000, \
        f'api visibility: {api_visibility} differs web visibility: {web_visibility}'

def verify_wind_speed_value(api_wind_speed, web_wind_speed):
    assert (api_wind_speed - web_wind_speed) <= 0.1, \
        f'api wind speed: {api_wind_speed} differs web wind speed: {web_wind_speed}'

def verify_pressure_value(api_pressure, web_pressure, tolerance):
    assert (api_pressure - web_pressure) <= tolerance, \
        f'api pressure: {api_pressure} differs web pressure: {web_pressure}'

def run_weather_verification(verify_city=True,
                             verify_temperature=True,
                             verify_feels_like=True,
                             verify_humidity=True,
                             verify_visibility=True,
                             verify_wind_speed=True,
                             verify_pressure=True,
                             ):
    tolerance = 1

    # Initialize the browser driver
    browser = Drivers('--ignore-certificate-errors').chrome()

    # Create an instance of the WeatherPage class
    web = WeatherPage(driver=browser)
    web.go()

    # Get current location from the web element
    city = web.city_name.text()

    # Call API to get weather data for the current location
    city_weather = GetWeather(city)

    if city_weather:
        api_city_name = city_weather['city_name']
        web_city_name = web.city_name.text()[:len(api_city_name)]

        if verify_city:
            verify_city_name(api_city_name, web_city_name)

        if verify_temperature:
            api_temperature = city_weather['temperature']
            web_temperature = float(''.join(filter(str.isdigit, web.temperature.text())))
            verify_temperature_value(api_temperature, web_temperature, tolerance)

        if verify_feels_like:
            api_feels_like = city_weather['feels_like']
            web_feels_like = float(re.findall(r'\d+', web.feels_like.text())[0])
            verify_feels_like_value(api_feels_like, web_feels_like, tolerance)

        if verify_humidity:
            api_humidity = city_weather['humidity']
            web_humidity = int(''.join(filter(str.isdigit, web.humidity.text())))
            verify_humidity_value(api_humidity, web_humidity)

        if verify_visibility:
            api_visibility = city_weather['visibility']
            web_visibility = float(web.visibility.text().split(':')[1].split('km')[0].strip())
            verify_visibility_value(api_visibility, web_visibility)

        if verify_wind_speed:
            api_wind_speed = city_weather[f'wind_speed']
            web_wind_speed = float(web.wind_speed.text().split('m/s')[0].strip())
            verify_wind_speed_value(api_wind_speed,web_wind_speed)

        if verify_pressure:
            api_pressure = city_weather['pressure']
            web_pressure = int(web.pressure.text()[:-3])
            verify_pressure_value(api_pressure, web_pressure, tolerance)

        # Call other verification functions for other weather attributes

        print('All weather verifications passed.')
    else:
        print('Weather data not available.')

    browser.quit()

# Example usage
run_weather_verification(verify_city=True,
                         verify_temperature=True,
                         verify_feels_like=True,
                         verify_humidity=True,
                         verify_visibility=True,
                         verify_wind_speed=True,
                         verify_pressure=True)
