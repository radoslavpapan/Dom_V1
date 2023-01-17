import socket, time, os, random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

UDP_PORT = 8888
UDP_IP = ''

try:
    f = open("IP.txt", "r")
    UDP_IP = f.read()
    f.close()
    print('Loaded IP: {}'.format(UDP_IP))
except FileNotFoundError:
    UDP_IP = input('Enter IP: ')
    f = open("IP.txt", "w+")
    f.write(UDP_IP)
    f.close()
    while 1:
        os.system("python main.py")
        time.sleep(0.2)

def sendUDP(dataToSend):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.settimeout(1.0 / 2.0)
    sock.sendto(str.encode(dataToSend), (UDP_IP, UDP_PORT))
    try:
        msgFromServer = sock.recvfrom(1024)
        sock.close()
        return msgFromServer[0].decode()
    except socket.timeout:
        sock.close()
        return "None"

# if sendUDP("c?") != 'OK':
#     UDP_IP = input('Enter IP: ')
#     f = open("IP.txt", "w+")
#     f.write(UDP_IP)
#     f.close()
#     while 1:
#         os.system("python main.py")
#         time.sleep(0.2)


class MyGridLayout(GridLayout):
    def button_press(self):
        Clock.schedule_interval(self.MainFunc, 1.0 / 1.0)


    def MainFunc(self, data):
        self.ids.label_TempOUT.text = str(sendUDP('TempOUT?')) + '°C'
        self.ids.label_HummOUT.text = str(sendUDP('HummOUT?')) + '%'
        self.ids.label_SpeedWIND.text = str(sendUDP('SpeedWIND?')) + 'm/s'
        self.ids.label_HummSOIL.text = str(sendUDP('HummSOIL?')) + '%'
        self.ids.label_LightOUT.text = str(sendUDP('LightOUT?')) + '%'

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    MyApp().run()