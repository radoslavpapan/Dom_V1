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
UDP_IP = '1.1.1.1'

def get_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # doesn't even have to be reachable
        sock.connect(('10.255.255.255', 1))
        IP = sock.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        sock.close()
    return IP

def changeIP():
    IP = get_ip().split('.')
    msgFromServer = ""
    for a in range(2, 255):
        IPc = IP[0] + '.' + IP[1] + '.' + IP[2] + '.' + str(a)
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        sock.settimeout(1.0 / 4.0)
        sock.sendto(b'c?', (IPc, UDP_PORT))
        try:
            msgFromServer = sock.recvfrom(1024)
            if msgFromServer[0].decode() == 'OK':
                f = open("IP.txt", "w+")
                f.write(IPc)
                f.close()
                UDP_IP = IPc
                return 0
        except socket.timeout:
            print(IPc)
            pass
        except ConnectionResetError:
            pass
        sock.close()

try:
    f = open("IP.txt", "r")
    UDP_IP = f.read().replace('\n', '')
    f.close()
    print('Loaded IP: {}'.format(UDP_IP))
except FileNotFoundError:
    pass

def sendUDP(dataToSend):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        while sock.recv(32): pass
    except:
        pass
    sock.settimeout(1.0 / 1.0)
    sock.sendto(str.encode(dataToSend), (UDP_IP, UDP_PORT))
    try:
        msgFromServer = sock.recvfrom(32)
        sock.close()
        return msgFromServer[0].decode()
    except socket.timeout:
        sock.close()
        return "None"

green = [0, 1, 0, .4]
red = [1, 0, 0, .4]
blue = [0, .85, 1, 1]
default = [1, 1, 1, 1]

class MyGridLayout(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.check_connection)
        Clock.schedule_interval(self.check_connection, 10.0 / 1.0)

    def close_all_ClockSchedule(self):
        Clock.unschedule(self.check_connection)
        Clock.unschedule(self.load_Input_data_loop)
        Clock.unschedule(self.load_data_loop)

    def start_all_ClockSchedule(self):
        Clock.schedule_interval(self.check_connection, 10.0 / 1.0)
        Clock.schedule_interval(self.load_Input_data_loop, 1.0 / 4.0)
        Clock.schedule_interval(self.load_data_loop, 5.0 / 1.0)

    def close_api(self):
        exit()

    def reboot_system(self):
        os.system("sudo reboot")

    def refresh_ip_release(self):
        self.ids.label_UDP_IP.text = 'Wait'
        changeIP()
        self.ids.label_UDP_IP.text = UDP_IP

    def refresh_ip_press(self):
        self.ids.label_UDP_IP.text = 'Wait...'

    def check_connection(self, data):
        if sendUDP('c?') == 'OK':
            self.ids.connection_stat_picture.source = "check.png"
            self.ids.connection_stat_label.text = "Connected"
            self.ids.connection_stat_label.background_color = green
            self.ids.UDP_IP_label.text = UDP_IP
            Clock.schedule_interval(self.load_Input_data_loop, 1.0 / 3.0)
            Clock.schedule_interval(self.load_data_loop, 5.0 / 1.0)
        else:
            self.ids.connection_stat_picture.source = "excl_mark.png"
            self.ids.connection_stat_label.text = "Disconnected"
            self.ids.connection_stat_label.background_color = red
            self.ids.UDP_IP_label.text = ''
            Clock.unschedule(self.load_Input_data_loop)
            Clock.unschedule(self.load_data_loop)

    def open_small_gate(self):
        self.close_all_ClockSchedule()
        sendUDP('D28 1!')
        time.sleep(3)
        sendUDP('D28 0!')
        self.start_all_ClockSchedule()

    def load_OUT_stat(self):
        try:
            DO = str(sendUDP('DOa?'))
            if DO[0] == '1':
                self.ids.D28_switch.active = True
            else:
                self.ids.D28_switch.active = False
            if DO[1] == '1':
                self.ids.D29_switch.active = True
            else:
                self.ids.D29_switch.active = False
            if DO[2] == '1':
                self.ids.D30_switch.active = True
            else:
                self.ids.D30_switch.active = False
            if DO[3] == '1':
                self.ids.D31_switch.active = True
            else:
                self.ids.D31_switch.active = False
            if DO[4] == '1':
                self.ids.D32_switch.active = True
            else:
                self.ids.D32_switch.active = False
            if DO[5] == '1':
                self.ids.D33_switch.active = True
            else:
                self.ids.D33_switch.active = False
            if DO[6] == '1':
                self.ids.D34_switch.active = True
            else:
                self.ids.D34_switch.active = False
            if DO[7] == '1':
                self.ids.D35_switch.active = True
            else:
                self.ids.D35_switch.active = False
            if DO[8] == '1':
                self.ids.D37_switch.active = True
            else:
                self.ids.D37_switch.active = False
            if DO[9] == '1':
                self.ids.D38_switch.active = True
            else:
                self.ids.D38_switch.active = False
            if DO[10] == '1':
                self.ids.D39_switch.active = True
            else:
                self.ids.D39_switch.active = False
            if DO[11] == '1':
                self.ids.D40_switch.active = True
            else:
                self.ids.D40_switch.active = False
            if DO[12] == '1':
                self.ids.D41_switch.active = True
            else:
                self.ids.D41_switch.active = False
            if DO[13] == '1':
                self.ids.D42_switch.active = True
            else:
                self.ids.D42_switch.active = False
            if DO[14] == '1':
                self.ids.D43_switch.active = True
            else:
                self.ids.D43_switch.active = False
            if DO[15] == '1':
                self.ids.D44_switch.active = True
            else:
                self.ids.D44_switch.active = False
        except:
            pass

    def LogIn(self):
        if self.ids.login_button.state == 'down':
            if self.ids.login_password.text == '0000':
                self.ids.login_password.text = ''
                self.ids.login_button.text = 'LogOut'
                self.ids.manual_OUT_tab.disabled = False
                self.load_OUT_stat()
            else:
                self.ids.login_button.state = 'normal'
                self.ids.login_password.text = ''
        if self.ids.login_button.state == 'normal':
            self.ids.login_button.text = 'LogIn'
            self.ids.manual_OUT_tab.disabled = True

    def D28_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D28 1!')
        else:
            sendUDP('D28 0!')
    def D29_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D29 1!')
        else:
            sendUDP('D29 0!')
    def D30_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D30 1!')
        else:
            sendUDP('D30 0!')
    def D31_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D31 1!')
        else:
            sendUDP('D31 0!')
    def D32_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D32 1!')
        else:
            sendUDP('D32 0!')
    def D33_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D33 1!')
        else:
            sendUDP('D33 0!')
    def D34_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D34 1!')
        else:
            sendUDP('D34 0!')
    def D35_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D35 1!')
        else:
            sendUDP('D35 0!')
    def D37_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D37 1!')
        else:
            sendUDP('D37 0!')
    def D38_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D38 1!')
        else:
            sendUDP('D38 0!')
    def D39_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D39 1!')
        else:
            sendUDP('D39 0!')
    def D40_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D40 1!')
        else:
            sendUDP('D40 0!')
    def D41_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D41 1!')
        else:
            sendUDP('D41 0!')
    def D42_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D42 1!')
        else:
            sendUDP('D42 0!')
    def D43_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D43 1!')
        else:
            sendUDP('D43 0!')
    def D44_manual_switch(self, switchobject, switchvalue):
        if switchvalue:
            sendUDP('D44 1!')
        else:
            sendUDP('D44 0!')

    def smart_heating_switch(self, switchobject, switchvalue):
        if switchvalue:
            Clock.schedule_interval(self.smart_heating_loop, 1.0 / 1.0)
        else:
            Clock.unschedule(self.smart_heating_loop)

    def smart_blinds_switch(self, switchobject, switchvalue):
        if switchvalue:
            Clock.schedule_interval(self.smart_blinds_loop, 1.0 / 1.0)
        else:
            Clock.unschedule(self.smart_blinds_loop)

    def smart_irrigation_switch(self, switchobject, switchvalue):
        if switchvalue:
            Clock.schedule_interval(self.smart_irrigation_loop, 1.0 / 1.0)
        else:
            Clock.unschedule(self.smart_irrigation_loop)

    def smart_heating_loop(self, data):
        print('Smart Heating...')

    def smart_blinds_loop(self, data):
        print('Smart Blinds...')

    def smart_irrigation_loop(self, data):
        print('Smart Irrigation...')

    def load_data_loop(self, data):
        self.ids.TempOUT_label.text = str(sendUDP('TempOUT?')) + '°C'
        self.ids.HummOUT_label.text = str(sendUDP('HummOUT?')) + '%'
        self.ids.SpeedWIND_label.text = str(sendUDP('SpeedWIND?')) + 'm/s'
        self.ids.HummSOIL_label.text = str(sendUDP('HummSOIL?')) + '%'
        self.ids.LightOUT_label.text = str(sendUDP('LightOUT?')) + '%'

    def load_Input_data_loop(self, data):
        start = time.time()
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
        except:
            pass
        end = time.time()
        print('{}ms'.format(int((end - start)*1000)))


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__=='__main__':

    MyApp().run()