from notify_run import Notify
import requests

def wttr():
    url = 'http://wttr.in/?format=%l:+%c+%t\nSunrise:%S\nSunset:%s\nDusk:%d\n%m'
    response = requests.get(url)
    data = response.text
    return data

notify = Notify(endpoint="https://notify.run/PUdK0BvYeMmYTMWE")
inf =notify.info()
notify.send(wttr())
print (inf)
