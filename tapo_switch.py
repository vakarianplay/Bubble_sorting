import argparse
from PyP100 import PyP100


def onDevice():
    p100.turnOn()
    print("Устройство включено")

def offDevice():
    p100.turnOff()
    print("Устройство выключено")

def toggleDevice():
    p100.toggleState()
    print("Устройство переключилось")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", help="Состояние устройства")

    args = parser.parse_args()

    p100 = PyP100.P100("192.168.X.X", "email@gmail.com", "Password123")
    p100.handshake()
    p100.login()


    if args.state == "on":
        onDevice()
    elif args.state == "off":
        offDevice()
    elif args.state == "toggle":
        toggleDevice()
    else:
        print("Неверное значение аргумента --state")
