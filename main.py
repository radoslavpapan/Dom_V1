import socket, time, os
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

os.system("python3 /home/pi/getdata.py &")

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
                with open("IP.txt", "w+") as f:
                    f.write(IPc)
                global UDP_IP
                UDP_IP = IPc
                return 0
        except socket.timeout:
            print(IPc)
            pass
        except ConnectionResetError:
            pass
        sock.close()

try:
    with open("IP.txt", "r") as f:
        UDP_IP = f.read().replace('\n', '')
    print('Loaded IP: {}'.format(UDP_IP))
except FileNotFoundError:
    pass

def sendUDP(dataToSend):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # try:
    #     while sock.recv(32):
    #         pass
    # except:
    #     pass
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

    def close_api(self):
        os.system("pkill -f smartheating.py")
        os.system("pkill -f smartblinds.py")
        os.system("pkill -f smartirrigation.py")
        os.system("pkill -f getdata.py")
        exit()

    def reboot_system(self):
        os.system("sudo reboot")

    def shutdown_system(self):
        os.system("sudo shutdown now")
    def update_system(self):
        os.system("sudo rm -f /home/pi/main.py")
        os.system("sudo rm -f /home/pi/my.kv")
        os.system("sudo rm -f /home/pi/getdata.py")
        os.system("sudo rm -f /home/pi/smartblinds.py")
        os.system("sudo rm -f /home/pi/smartheating.py")
        os.system("sudo rm -f /home/pi/smartirrigation.py")
        os.system("sudo rm -f /home/pi/main.py")
        os.system("sudo rm -r Dom_V1")
        os.system("sudo git clone https://github.com/radoslavpapan/Dom_V1.git")
        os.system("sudo mv -f /home/pi/Dom_V1/main.py /home/pi")
        os.system("sudo mv -f /home/pi/Dom_V1/my.kv /home/pi")
        os.system("sudo mv -f /home/pi/Dom_V1/getdata.py /home/pi")
        os.system("sudo mv -f /home/pi/Dom_V1/smartblinds.py /home/pi")
        os.system("sudo mv -f /home/pi/Dom_V1/smartheating.py /home/pi")
        os.system("sudo mv -f /home/pi/Dom_V1/smartirrigation.py /home/pi")
        os.system("sudo rm -r Dom_V1")
        print("Update complete")

    def refresh_ip_release(self):
        self.ids.label_UDP_IP.text = 'Wait'
        changeIP()
        self.ids.label_UDP_IP.text = UDP_IP
        Clock.schedule_once(self.check_connection)

    def refresh_ip_press(self):
        self.ids.label_UDP_IP.text = 'Wait...'

    def check_connection(self, data):
        if sendUDP('c?') == 'OK':
            self.ids.connection_stat_picture.source = "check.png"
            self.ids.connection_stat_label.text = "Connected"
            self.ids.connection_stat_label.background_color = green
            self.ids.UDP_IP_label.text = UDP_IP
            Clock.schedule_interval(self.MainLoop, 1.0 / 1.0)
        else:
            self.ids.connection_stat_picture.source = "excl_mark.png"
            self.ids.connection_stat_label.text = "Disconnected"
            self.ids.connection_stat_label.background_color = red
            self.ids.UDP_IP_label.text = ''

    def open_small_gate(self):
        Clock.unschedule(self.MainLoop)
        if sendUDP('D28 1!') != '1':
            if sendUDP('D28 1!') != '1':
                pass
        time.sleep(3)
        sendUDP('D28 0!')
        Clock.schedule_interval(self.MainLoop, 1.0 / 1.0)

    def open_big_gate_press(self):
        if sendUDP('D29 1!') != '1':
            sendUDP('D29 1!')

    def open_big_gate_release(self):
        if sendUDP('D29 0!') != '0':
            sendUDP('D29 0!')

    def load_output_stat(self):
        try:
            with open("SharedData.txt", "r") as f:
                LoadedData = f.readlines()
            for i in LoadedData:
                dat = i.split(";")
                if dat[0] == 'D28':
                    if dat[1] == '1':
                        self.ids.D28_switch.active = True
                    else:
                        self.ids.D28_switch.active = False
                elif dat[0] == 'D29':
                    if dat[1] == '1':
                        self.ids.D29_switch.active = True
                    else:
                        self.ids.D29_switch.active = False
                elif dat[0] == 'D30':
                    if dat[1] == '1':
                        self.ids.D30_switch.active = True
                    else:
                        self.ids.D30_switch.active = False
                elif dat[0] == 'D31':
                    if dat[1] == '1':
                        self.ids.D31_switch.active = True
                    else:
                        self.ids.D31_switch.active = False
                elif dat[0] == 'D32':
                    if dat[1] == '1':
                        self.ids.D32_switch.active = True
                    else:
                        self.ids.D32_switch.active = False
                elif dat[0] == 'D33':
                    if dat[1] == '1':
                        self.ids.D33_switch.active = True
                    else:
                        self.ids.D33_switch.active = False
                elif dat[0] == 'D34':
                    if dat[1] == '1':
                        self.ids.D34_switch.active = True
                    else:
                        self.ids.D34_switch.active = False
                elif dat[0] == 'D35':
                    if dat[1] == '1':
                        self.ids.D35_switch.active = True
                    else:
                        self.ids.D35_switch.active = False
                elif dat[0] == 'D37':
                    if dat[1] == '1':
                        self.ids.D37_switch.active = True
                    else:
                        self.ids.D37_switch.active = False
                elif dat[0] == 'D38':
                    if dat[1] == '1':
                        self.ids.D38_switch.active = True
                    else:
                        self.ids.D38_switch.active = False
                elif dat[0] == 'D39':
                    if dat[1] == '1':
                        self.ids.D39_switch.active = True
                    else:
                        self.ids.D39_switch.active = False
                elif dat[0] == 'D40':
                    if dat[1] == '1':
                        self.ids.D40_switch.active = True
                    else:
                        self.ids.D40_switch.active = False
                elif dat[0] == 'D41':
                    if dat[1] == '1':
                        self.ids.D41_switch.active = True
                    else:
                        self.ids.D41_switch.active = False
                elif dat[0] == 'D42':
                    if dat[1] == '1':
                        self.ids.D42_switch.active = True
                    else:
                        self.ids.D42_switch.active = False
                elif dat[0] == 'D43':
                    if dat[1] == '1':
                        self.ids.D43_switch.active = True
                    else:
                        self.ids.D43_switch.active = False
                elif dat[0] == 'D44':
                    if dat[1] == '1':
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
                self.ids.close_API_button.disabled = False
                self.ids.conf_API_button.disabled = False
                self.load_output_stat()
            else:
                self.ids.login_button.state = 'normal'
                self.ids.login_password.text = ''
        if self.ids.login_button.state == 'normal':
            self.ids.login_button.text = 'LogIn'
            self.ids.manual_OUT_tab.disabled = True
            self.ids.close_API_button.disabled = True
            self.ids.conf_API_button.disabled = True

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
            os.system("python3 /home/pi/smartheating.py &")
        else:
            os.system("pkill -f smartheating.py")

    def smart_blinds_switch(self, switchobject, switchvalue):
        if switchvalue:
            os.system("python3 /home/pi/smartblinds.py &")
        else:
            os.system("pkill -f smartblinds.py")

    def smart_irrigation_switch(self, switchobject, switchvalue):
        if switchvalue:
            os.system("python3 /home/pi/smartirrigation.py &")
        else:
            os.system("pkill -f smartirrigation.py")

    def MainLoop(self, data):
        try:
            with open("SharedData.txt", "r") as f:
                LoadedData = f.readlines()
            for i in LoadedData:
                dat = i.split(";")
                if dat[0] == 'TempOUT':
                    self.ids.TempOUT_label.text = dat[1] + '°C'
                elif dat[0] == 'HummOUT':
                    self.ids.HummOUT_label.text = dat[1] + '%'
                elif dat[0] == 'SpeedWIND':
                    self.ids.SpeedWIND_label.text = dat[1] + 'm/s'
                elif dat[0] == 'HummSOIL':
                    self.ids.HummSOIL_label.text = dat[1] + '%'
                elif dat[0] == 'LightOUT':
                    self.ids.LightOUT_label.text = dat[1] + '%'
                elif dat[0] == 'D2':
                    self.ids.label_D2.text = dat[1]
                elif dat[0] == 'D3':
                    self.ids.label_D3.text = dat[1]
                elif dat[0] == 'D4':
                    self.ids.label_D4.text = dat[1]
                elif dat[0] == 'D5':
                    self.ids.label_D5.text = dat[1]
                elif dat[0] == 'D6':
                    self.ids.label_D6.text = dat[1]
                elif dat[0] == 'D7':
                    self.ids.label_D7.text = dat[1]
                elif dat[0] == 'D16':
                    self.ids.label_D16.text = dat[1]
                elif dat[0] == 'D17':
                    self.ids.label_D17.text = dat[1]
                elif dat[0] == 'D26':
                    self.ids.label_D26.text = dat[1]
                elif dat[0] == 'D27':
                    self.ids.label_D27.text = dat[1]
                elif dat[0] == 'D36':
                    self.ids.label_D36.text = dat[1]
        except:
            pass

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    MyApp().run()