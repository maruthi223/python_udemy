import requests
import datetime as dt
my_lat = 17.492118
my_lng = 78.318268

def is_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    lat = float(data['iss_position']['latitude'])
    lon = float(data['iss_position']['longitude'])

    iss_position = (lat,lon)
    print(iss_position)
    if my_lat-5 < lat < my_lat+5 and my_lng-5<lon<my_lng+5:
        return True
def is_night():
    parameters = {
        'lat': my_lat,
        'lng': my_lng,
        'formatted': 0
    }
    response1 = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    response1.raise_for_status()
    data1 = response1.json()
    sunrise = int(data1['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data1['results']['sunset'].split('T')[1].split(':')[0])

    time = dt.datetime.now().hour
    if time >=sunset and time<=sunrise:
        return True
    
if is_overhead and is_night:
    pass # you can send the mail using smtplib