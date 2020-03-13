import pytest
import requests
import os


base_url = "http://samples.openweathermap.org/data/2.5/find?"

@pytest.fixture
def endpoint():
    API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    test_url = "{}q=Toronto,ca&units=metric&appid={}".format(base_url, API_KEY)
    return test_url


def test_service_is_up(endpoint):
    response = requests.get(endpoint)

    assert response.status_code == 200

def test_service_shows_current_temperature(endpoint):
    response = requests.get(endpoint)
    body = response.json()

    current_temp = body['list'][0]['main']['temp']
    
    assert current_temp is not None
