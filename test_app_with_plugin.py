import pytest

# @pytest.fixture
# def selenium():
#   ...clever things here...
#   return webdriver

def test_message_appears(selenium):
    selenium.get("http://localhost:3000")

    selenium.find_element_by_class_name('scale-type-c').send_keys('0')

    assert selenium.find_element_by_class_name('temperatureMesssage').is_displayed()

def test_message_is_correct(selenium):
    selenium.get("http://localhost:3000")

    selenium.find_element_by_class_name('scale-type-c').send_keys('0')

    assert selenium.find_element_by_class_name('temperatureMesssage').text == '0 Celsius is 32 Fahrenheit'
