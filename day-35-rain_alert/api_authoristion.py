import requests

key = ''
my_lat = 17.492118
my_lng = 78.318268
parameter = {
    'lat' : my_lat,
    'lng' : my_lng,
    'appid': key
}

response = requests.get(url='https://api.openweathermap.org/data/3.0/onecall', params=parameter)
response.raise_for_status()
data = response.json()
weather = data['hourly'][:12] # gives from hour 0 to 11

will_rain = False
for hour in weather:
    condition = hour['weather'][0]['id']
    if int(condition) < 700:
        will_rain = True
if will_rain:

    print('take your umbrella')
