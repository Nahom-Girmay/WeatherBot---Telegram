import requests

from config import WEATHER_API_KEY


def get_weather(city):

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)
    weather = response.json()

    if "error" in weather:
        return None

    return {
        "city": weather["location"]["name"],
        "country": weather["location"]["country"],
        "temperature": weather["current"]["temp_c"],
        "condition": weather["current"]["condition"]["text"],
        "humidity": weather["current"]["humidity"],
        "wind": weather["current"]["wind_kph"]
    }


def get_forecast(city):

    url = "https://api.weatherapi.com/v1/forecast.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "days": 3
    }

    response = requests.get(url, params=params)
    forecast = response.json()

    if "error" in forecast:
        return None

    forecast_days = forecast["forecast"]["forecastday"]

    result = []

    for day in forecast_days:
        result.append({
            "date": day["date"],
            "temperature": day["day"]["avgtemp_c"],
            "condition": day["day"]["condition"]["text"]
        })

    return result