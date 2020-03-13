import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    d = webdriver.Firefox()
    yield d
    d.quit()

def test_message_appears(browser):
    browser.get("http://localhost:3000")

    browser.find_element_by_class_name('scale-type-c').send_keys('0')

    assert browser.find_element_by_class_name('temperatureMesssage').is_displayed()

def test_message_is_correct(browser):
    browser.get("http://localhost:3000")

    browser.find_element_by_class_name('scale-type-c').send_keys('0')

    assert browser.find_element_by_class_name('temperatureMesssage').text == '0 Celsius is 32 Fahrenheit'