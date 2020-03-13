class TemperatureConverter(object):

    def to_celsius(self, far):
        return (far - 32.0)/1.8

    def to_fahrenheit(self, cel):
        return cel*1.8 + 32.0
