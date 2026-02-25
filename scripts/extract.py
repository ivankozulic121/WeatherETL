import requests

def extract_towns():
    towns_list = ["Berlin","Frankfurt","Hamburg","New York","Los Angeles","London","Paris","Tokyo",
    "Moscow","San Francisco","New Delhi","Beijing","Chicago","Milan","Rome"]

    towns_data = []

    for town in towns_list:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={town}&count=10&language=en&format=json"
        response = requests.get(url)
        data = response.json()
        for item in data["results"]:
            towns_data.append(
                {
                    "city_id": item["id"],
                    "city_name": item["name"],
                    "country": item["country"],
                    "latitude": item["latitude"],
                    "longitude": item["longitude"]
                }
            )

    return towns_data


def extract_weather_data():
    towns_data = extract_towns()
    weather_data = []
    baseURL = "https://api.open-meteo.com/v1/forecast"

    for town in towns_data:
        response = requests.get(f"{baseURL}?latitude={town['latitude']}&longitude={town['longitude']}&current=temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m")
        data = response.json()
        current_weather = data.get("current")
        weather_data.append(
            {
                "temperature": current_weather.get('temperature_2m'),
                "humidity": current_weather.get('relative_humidity_2m'),
                "pressure": current_weather.get('surface_pressure'),
                "wind_speed": current_weather.get('wind_speed_10m'),
            }
        )
    return weather_data




