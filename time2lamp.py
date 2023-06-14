import requests
import time
import re
from pyA20.gpio import gpio
from pyA20.gpio import port


def get_dusk():
    url = 'http://wttr.in/?format=%d'
    response_dusk = requests.get(url)
    dusk = response_dusk.text
    dusk = re.findall(r'\b[0-2]?\d:[0-5]\d\b', dusk)[0]
    return dusk

def get_dawn():
    url = 'http://wttr.in/?format=%D'
    response_dawn = requests.get(url)
    dawn = response_dawn.text
    dawn = re.findall(r'\b[0-2]?\d:[0-5]\d\b', dawn)[0]
    return dawn

led = port.LED
gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

dusktime = get_dusk()
dawntime = get_dawn()
status = 0

while True:
    current_time = time.strftime("%H:%M")
    print(current_time)
    if dusktime < current_time and status == 0:
        print('work')
        gpio.output(led, 1)
        status = 1
    elif dawntime > current_time and status == 1:
        print ('off')
         gpio.output(led, 0)
        status = 0
    elif current_time == ("13:25"):
        print ('update time: success')
        dusktime = get_dusk()
        dawntime = get_dawn()
        time.sleep(60)
    else:
        print('not time')

    time.sleep(5)
