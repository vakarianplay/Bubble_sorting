from notify_run import Notify
import requests

#get weather data
def wttr():
    url = 'http://wttr.in/?format=%l:+%c+%t\nSunrise:%S\nSunset:%s\nDusk:%d\n%m'
    response = requests.get(url)
    data = response.text
    return data

#connect push channel
notify = Notify(endpoint="https://notify.run/PUdK0BvYeMmYTMWE")
#info about channel
inf =notify.info()
#send data
notify.send(wttr())
print (inf)
