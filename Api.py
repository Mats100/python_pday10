import requests
My_lat = 36.7201600
My_long = -4.4203400

parameters = {
    "lat": My_lat,
    "lng": My_long
}

response = requests.get("https://api.sunrise-sunset.org/json.",params=parameters)
response.raise_for_status()
data = response.json()
print(data)