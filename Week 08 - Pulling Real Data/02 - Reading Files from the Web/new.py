import requests
url = "https://api.open-meteo.com/v1/forecast"
params= {"latitude":25.2048, "longitude": 55.2708, "current_weather": True}
response = requests.get(url, params=params, timeout=10)
print(response.status_code)
if response.status_code ==200:
    data = response.json()
    current = data.get("current_weather", {})
    print("Temperature:", current.get("temperature", "N/A"))
    print("Windspeed:", current.get("windspeed", "N/A"))

else:
    print("Request failed")
