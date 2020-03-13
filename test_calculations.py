from calculations import TemperatureConverter


def testfreezing_fahrenheit():
    converter = TemperatureConverter()

    actual = converter.to_celsius(32.0)
    expected = 0.0

    assert abs(expected - actual) < 0.01

def test_freezing_celsius():
    converter = TemperatureConverter()

    actual = converter.to_fahrenheit(0)
    expected = 32.0

    assert abs(expected - actual) < 0.01
