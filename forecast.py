import requests

from config import API_KEY


FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_forecast(city):
    """Retrieve future weather data for a city."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        return {
            "success": True,
            "forecasts": data["list"]
        }

    except requests.RequestException:
        return {
            "success": False,
            "error": "Unable to retrieve forecast data."
        }
    

def analyse_upcoming_weather(forecasts, hours_ahead=12):
    """
    Analyse upcoming forecast entries and return useful warnings.

    Each forecast entry covers approximately three hours.
    """

    entries_to_check = max(1, hours_ahead // 3)
    upcoming_entries = forecasts[:entries_to_check]

    rain_expected = False
    snow_expected = False
    strongest_wind = 0
    lowest_temperature = None
    rain_time = None

    for entry in upcoming_entries:
        description = entry["weather"][0]["description"].lower()
        wind_speed = entry["wind"]["speed"]
        temperature = entry["main"]["temp"]

        if lowest_temperature is None or temperature < lowest_temperature:
            lowest_temperature = temperature

        strongest_wind = max(strongest_wind, wind_speed)

        if "rain" in description or "drizzle" in description:
            rain_expected = True

            if rain_time is None:
                rain_time = entry["dt_txt"]

        if "snow" in description:
            snow_expected = True

    return {
        "rain_expected": rain_expected,
        "rain_time": rain_time,
        "snow_expected": snow_expected,
        "strongest_wind": strongest_wind,
        "lowest_temperature": lowest_temperature
    }