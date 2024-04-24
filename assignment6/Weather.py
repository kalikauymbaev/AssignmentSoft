# Common Data Model for Weather
class WeatherData:
    def __init__(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def __str__(self):
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Wind Speed: {self.wind_speed} km/h"

# Adapter Interface
class WeatherAdapter:
    def get_weather_data(self):
        raise NotImplementedError("Each adapter must implement the `get_weather_data` method.")

# Concrete Adapter for API A
class APIAAdapter(WeatherAdapter):
    def __init__(self, api_a):
        self.api_a = api_a

    def get_weather_data(self):
        data = self.api_a.fetch_data()
        # Convert temperature from Fahrenheit to Celsius
        temperature_c = (data['temperature_f'] - 32) * 5.0/9.0
        return WeatherData(temperature_c, data['humidity_percent'], data['wind_speed_kmh'])

# Concrete Adapter for API B
class APIBAdapter(WeatherAdapter):
    def __init__(self, api_b):
        self.api_b = api_b

    def get_weather_data(self):
        data = self.api_b.get_current_weather()
        # API B data already in Celsius
        return WeatherData(data['temp_c'], data['humidity'], data['wind'])

# Simulating External Weather API A
class API_A:
    def fetch_data(self):
        return {"temperature_f": 78, "humidity_percent": 50, "wind_speed_kmh": 10}

# Simulating External Weather API B
class API_B:
    def get_current_weather(self):
        return {"temp_c": 25, "humidity": 55, "wind": 5}

# Testing the Adapter Implementation
if __name__ == "__main__":
    # Instantiate APIs
    api_a = API_A()
    api_b = API_B()

    # Create adapters
    adapter_a = APIAAdapter(api_a)
    adapter_b = APIBAdapter(api_b)

    # Fetch and display weather data using adapters
    print("Weather from API A:", adapter_a.get_weather_data())
    print("Weather from API B:", adapter_b.get_weather_data())
