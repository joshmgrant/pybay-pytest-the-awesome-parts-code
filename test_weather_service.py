import requests
import os


def test_service_is_up():
    API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    test_url = "http://samples.openweathermap.org/data/2.5/find?q=Toronto,ca&units=metric&appid={}".format(API_KEY)

    response = requests.get(test_url)

    assert response.status_code == 200

def test_service_shows_current_temperature():
    API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    test_url = "http://samples.openweathermap.org/data/2.5/find?q=Toronto,ca&units=metric&appid={}".format(API_KEY)

    response = requests.get(test_url)
    body = response.json()

    current_temp = body['list'][0]['main']['temp']
    
    assert current_temp is not None
