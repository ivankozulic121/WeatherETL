import requests

def extract_towns():
    towns_list = ["Berlin","Frankfurt","Hamburg","New York","Los Angeles","London","Paris","Tokyo",
    "Moscow","San Francisco","New Delhi","Beijing","Chicago","Milan","Rome"]

    towns_data = []

    for town in towns_list:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={town}&count=10&language=en&format=json"
        response = requests.get(url)
        data = response.json()
        #print(data)
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


