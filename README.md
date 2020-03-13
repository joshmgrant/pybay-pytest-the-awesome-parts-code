# PyBay Meetup - PyTest: The Awesome Parts: The Code
------------------------

Here is the code I used in my live coding sessions at the (virtual) PyBay Meetup on March 11, 2020. If you attended that meetup and liked my talk, thanks so much!

To get started, install all the dependencies here using:

```
pip install -r requirements.txt
```

All code samples here use Python 3.6 and have not been tested on lower versions of Python. 

## Running tests

To run the unit test examples, run

```
pytest test_calculations.py
```

which is fast and easy. 

To run the API/Service test example, run

```
pytest test_weather_service.py
```

or

```
pytest test test_fixture_weather_service.py
```

These API tests may not execute properly if you

- do not have an internet connection,
- if you cannot access the openweathermap.com API, or 
- if you do not have a configured API key for openweathermap.com. 

Please see [the Open Weather Map API](https://openweathermap.org/api) for more details, or try updating these tests with your favourite API! 

To run the browser tests, you will need:

- The latest version of Firefox installed on your machine
- The latest version of the [Geckodriver](https://github.com/mozilla/geckodriver/releases) installed and added to your PATH
- A latest version of the [Selenium Server](https://www.selenium.dev/documentation/en/getting_started/quick/#webdriver) installed
- (Optionally) Safari, Chrome, IE or some other browser of interest
- (Optionally) A [Sauce Labs](www.saucelabs.com) account.

I've also included a sample app that you can start up to test against under the `sample_app` directory. To start this app up, you can use NodeJS and run

```
cd sample_app/
npm install
npm start
```

to start the test on `http://localhost:3000`.

After getting that set up, you can run the sample test hardcoded to use Firefox by running

```
pytest test_app.py
```

or using the pytest-selenium plugin test by running

```
pytest --driver Firefox test_app_with_plugin.py
```

Please see the [Pytest Selenium](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html) project for more infomation around these tests. 
