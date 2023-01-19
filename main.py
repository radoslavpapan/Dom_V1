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
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.config import ConfigParser
from kivy.uix.settings import SettingsWithTabbedPanel

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

green = [0, 1, 0, .4]
red = [1, 0, 0, .4]
blue = [0, .85, 1, 1]
default = [1, 1, 1, 1]

class MyGridLayout(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
        if sendUDP('c?') == 'OK':
            self.ids.connection_stat_picture.source = "check.png"
            self.ids.connection_stat_text.text = "Connected"
            self.ids.connection_stat_text.background_color = green
        else:
            self.ids.connection_stat_picture.source = "excl_mark.png"
            self.ids.connection_stat_text.text = "Disconnected"
            self.ids.connection_stat_text.background_color = red

    def D28_manual_button_press(self):
        if self.ids.D28_manual_button.state == 'down':
            sendUDP('D28 1!')
        elif self.ids.D28_manual_button.state == 'normal':
            sendUDP('D28 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D29_manual_button_press(self):
        if self.ids.D29_manual_button.state == 'down':
            sendUDP('D29 1!')
        elif self.ids.D29_manual_button.state == 'normal':
            sendUDP('D29 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D30_manual_button_press(self):
        if self.ids.D30_manual_button.state == 'down':
            sendUDP('D30 1!')
        elif self.ids.D30_manual_button.state == 'normal':
            sendUDP('D30 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D31_manual_button_press(self):
        if self.ids.D31_manual_button.state == 'down':
            sendUDP('D31 1!')
        elif self.ids.D31_manual_button.state == 'normal':
            sendUDP('D31 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D32_manual_button_press(self):
        if self.ids.D32_manual_button.state == 'down':
            sendUDP('D32 1!')
        elif self.ids.D32_manual_button.state == 'normal':
            sendUDP('D32 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D33_manual_button_press(self):
        if self.ids.D33_manual_button.state == 'down':
            sendUDP('D33 1!')
        elif self.ids.D33_manual_button.state == 'normal':
            sendUDP('D33 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D34_manual_button_press(self):
        if self.ids.D34_manual_button.state == 'down':
            sendUDP('D34 1!')
        elif self.ids.D34_manual_button.state == 'normal':
            sendUDP('D34 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D35_manual_button_press(self):
        if self.ids.D35_manual_button.state == 'down':
            sendUDP('D35 1!')
        elif self.ids.D35_manual_button.state == 'normal':
            sendUDP('D35 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D37_manual_button_press(self):
        if self.ids.D37_manual_button.state == 'down':
            sendUDP('D37 1!')
        elif self.ids.D37_manual_button.state == 'normal':
            sendUDP('D37 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D38_manual_button_press(self):
        if self.ids.D38_manual_button.state == 'down':
            sendUDP('D38 1!')
        elif self.ids.D38_manual_button.state == 'normal':
            sendUDP('D38 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D39_manual_button_press(self):
        if self.ids.D39_manual_button.state == 'down':
            sendUDP('D39 1!')
        elif self.ids.D39_manual_button.state == 'normal':
            sendUDP('D39 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D40_manual_button_press(self):
        if self.ids.D40_manual_button.state == 'down':
            sendUDP('D40 1!')
        elif self.ids.D40_manual_button.state == 'normal':
            sendUDP('D40 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D41_manual_button_press(self):
        if self.ids.D41_manual_button.state == 'down':
            sendUDP('D41 1!')
        elif self.ids.D41_manual_button.state == 'normal':
            sendUDP('D41 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D42_manual_button_press(self):
        if self.ids.D42_manual_button.state == 'down':
            sendUDP('D42 1!')
        elif self.ids.D42_manual_button.state == 'normal':
            sendUDP('D42 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D43_manual_button_press(self):
        if self.ids.D43_manual_button.state == 'down':
            sendUDP('D43 1!')
        elif self.ids.D43_manual_button.state == 'normal':
            sendUDP('D43 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)
    def D44_manual_button_press(self):
        if self.ids.D44_manual_button.state == 'down':
            sendUDP('D44 1!')
        elif self.ids.D44_manual_button.state == 'normal':
            sendUDP('D44 0!')
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)

    def button_press(self):
        Clock.schedule_interval(self.MainFunc, 2.0 / 1.0)


    def MainFunc2(self, data):
        print('skuska')

    def MainFunc(self, data):
        start = time.time()
        self.ids.label_TempOUT.text = str(sendUDP('TempOUT?')) + '°C'
        self.ids.label_HummOUT.text = str(sendUDP('HummOUT?')) + '%'
        self.ids.label_SpeedWIND.text = str(sendUDP('SpeedWIND?')) + 'm/s'
        self.ids.label_HummSOIL.text = str(sendUDP('HummSOIL?')) + '%'
        self.ids.label_LightOUT.text = str(sendUDP('LightOUT?')) + '%'
        try:
            DO = str(sendUDP('DIa?'))
            self.ids.label_D2.text = DO[0]
            self.ids.label_D3.text = DO[1]
            self.ids.label_D4.text = DO[2]
            self.ids.label_D5.text = DO[3]
            self.ids.label_D6.text = DO[4]
            self.ids.label_D7.text = DO[5]
            self.ids.label_D16.text = DO[6]
            self.ids.label_D17.text = DO[7]
            self.ids.label_D26.text = DO[8]
            self.ids.label_D27.text = DO[9]
            self.ids.label_D36.text = DO[10]
            DO = str(sendUDP('DOa?'))
            if DO[0] == '1':
                self.ids.D28_manual_button.state = 'down'
            else:
                self.ids.D28_manual_button.state = 'normal'
            if DO[1] == '1':
                self.ids.D29_manual_button.state = 'down'
            else:
                self.ids.D29_manual_button.state = 'normal'
            if DO[2] == '1':
                self.ids.D30_manual_button.state = 'down'
            else:
                self.ids.D30_manual_button.state = 'normal'
            if DO[3] == '1':
                self.ids.D31_manual_button.state = 'down'
            else:
                self.ids.D31_manual_button.state = 'normal'
            if DO[4] == '1':
                self.ids.D32_manual_button.state = 'down'
            else:
                self.ids.D32_manual_button.state = 'normal'
            if DO[5] == '1':
                self.ids.D33_manual_button.state = 'down'
            else:
                self.ids.D33_manual_button.state = 'normal'
            if DO[6] == '1':
                self.ids.D34_manual_button.state = 'down'
            else:
                self.ids.D34_manual_button.state = 'normal'
            if DO[7] == '1':
                self.ids.D35_manual_button.state = 'down'
            else:
                self.ids.D35_manual_button.state = 'normal'
            if DO[8] == '1':
                self.ids.D37_manual_button.state = 'down'
            else:
                self.ids.D37_manual_button.state = 'normal'
            if DO[9] == '1':
                self.ids.D38_manual_button.state = 'down'
            else:
                self.ids.D38_manual_button.state = 'normal'
            if DO[10] == '1':
                self.ids.D39_manual_button.state = 'down'
            else:
                self.ids.D39_manual_button.state = 'normal'
            if DO[11] == '1':
                self.ids.D40_manual_button.state = 'down'
            else:
                self.ids.D40_manual_button.state = 'normal'
            if DO[12] == '1':
                self.ids.D41_manual_button.state = 'down'
            else:
                self.ids.D41_manual_button.state = 'normal'
            if DO[13] == '1':
                self.ids.D42_manual_button.state = 'down'
            else:
                self.ids.D42_manual_button.state = 'normal'
            if DO[14] == '1':
                self.ids.D43_manual_button.state = 'down'
            else:
                self.ids.D43_manual_button.state = 'normal'
            if DO[15] == '1':
                self.ids.D44_manual_button.state = 'down'
            else:
                self.ids.D44_manual_button.state = 'normal'
        except:
            pass
        end = time.time()
        print(end - start)


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__=='__main__':

    MyApp().run()