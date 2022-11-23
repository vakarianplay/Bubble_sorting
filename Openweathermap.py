import re
import sys
from datetime import datetime
import requests

appid ="03d92e1dcdf06982a35783083f52690a"



def get_wind_direction(deg):
    l = ['С ','СВ',' В','ЮВ','Ю ','ЮЗ',' З','СЗ']
    for i in range(0,8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

# Запрос текущей погоды
def request_current_weather(city_id):
    print(city_id)
    try:
        opwRes = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        opwData = opwRes.json()
        caption = opwData['weather'][0]['description']
        currentTemp = str(opwData['main']['temp']) + " (" + str(opwData['main']['feels_like']) + ")"

        humidity = str(opwData['main']['humidity']) + " %"
        pressure = str(round(int(opwData['main']['pressure'])/1.33)) + " мм рт ст"
        wind = get_wind_direction(opwData['wind']['deg']) + " " + str(opwData['wind']['speed']) + " м/с"

        sunrise = datetime.utcfromtimestamp(opwData['sys']['sunrise'] + int(opwData['timezone'])).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(opwData['sys']['sunset'] + int(opwData['timezone'])).strftime('%H:%M:%S')

        print(sunrise)
        print(sunset)
        print(humidity)
        print(pressure)
        print(wind)
        print(caption)
        print(currentTemp)
    except Exception as e:
        print("Exception (weather):", e)
        pass

# Прогноз
def request_forecast(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        for i in data['list']:
            print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                   '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                   get_wind_direction(i['wind']['deg']),
                   i['weather'][0]['description'] )
    except Exception as e:
        print("Exception (forecast):", e)
        pass


request_current_weather(563523)
request_forecast(563523)
