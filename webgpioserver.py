import os
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.250'
host_port = 8000

def fileIndex():
    with open('index.html', encoding='utf-8') as myfile:
        data = myfile.read()
    return data

def htmlOn():
    html = '''
       <html>
       <head>
         <meta charset="UTF-8">
         <title>OPi Zero</title>
         <link rel="stylesheet" href="http://woa.aiq.ru/stylegpio.css">
         <link rel="preconnect" href="https://fonts.googleapis.com">
         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;1,400&display=swap');
        </style>
       </head>
       <body>
         <text><p> OPi Zero </p></text>
         <text><p> интерфейс </p></text>
           <br><br>
        <center><a href="/{relay}"><button class="btn" style="background:{back_relay};">Розетка <i class="fas fa-plug"></i></button></a></center>
        <br>
        <center><a href="/{radio}"><button class="btn" style="background:{back_radio};">Радио <i class="fas fa-radio"></i></button></a></center>
        <br>
        <br>
        <br>
        <br>
         <footer></footer>
         </body>
       </body>
       </html>
    '''
    return html

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("Content-type: text/html\n")
        statusMpc = os.popen("mpc current").read()
        stateRelay = int(os.popen("gpio read 7").read())
        if stateRelay == 0:
            relayHref = 'relayOff'
            relayColor = '#e0e0e0'
        if stateRelay == 1:
            relayHref = 'relayOn'
            relayColor = '#808080'

        if statusMpc == "":
            radioHref = 'radioOn'
            radioColor = '#808080'
        else:
            radioHref = 'radioOff'
            radioColor = '#e0e0e0'

        self.do_HEAD()

        replaceTemp = {'relay': relayHref, 'back_relay': relayColor, 'radio': radioHref, 'back_radio': radioColor}

        if self.path=='/':
            print('root')
            print(statusMpc)

        elif self.path=='/relayOn':
            os.system("gpio write 7 0")
            relayHref = 'relayOff'
            relayColor = '#e0e0e0'
            replaceTemp = {'relay': relayHref, 'back_relay': relayColor, 'radio': radioHref, 'back_radio': radioColor}

        elif self.path=='/relayOff':
            os.system("gpio write 7 1")
            relayHref = 'relayOn'
            relayColor = '#808080'
            replaceTemp = {'relay': relayHref, 'back_relay': relayColor, 'radio': radioHref, 'back_radio': radioColor}

        elif self.path=='/radioOn':
            os.system("mpc play 1")
            radioHref = 'radioOff'
            radioColor = '#e0e0e0'
            replaceTemp = {'relay': relayHref, 'back_relay': relayColor, 'radio': radioHref, 'back_radio': radioColor}

        elif self.path=='/radioOff':
            os.system("mpc stop")
            radioHref = 'radioOn'
            radioColor = '#808080'
            replaceTemp = {'relay': relayHref, 'back_relay': relayColor, 'radio': radioHref, 'back_radio': radioColor}

        self.wfile.write(htmlOn().format(**replaceTemp).encode("utf-8"))

        # self.wfile.write(html.format.encode("utf-8"))



if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
