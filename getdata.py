import socket
import time

UDP_PORT = 8888
UDP_IP = '1.1.1.1'

try:
    with open("IP.txt", "r") as f:
        UDP_IP = f.read().replace('\n', '')
except FileNotFoundError:
    pass

def sendUDP(dataToSend):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.settimeout(1.0 / 1.0)
    sock.sendto(str.encode(dataToSend), (UDP_IP, UDP_PORT))
    try:
        msgFromServer = sock.recvfrom(32)
        sock.close()
        return msgFromServer[0].decode()
    except socket.timeout:
        sock.close()
        return "None"

try:
    while True:
        DI = str(sendUDP('DIa?'))
        DO = str(sendUDP('DOa?'))
        TempOUT = str(sendUDP('TempOUT?'))
        HummOUT = str(sendUDP('HummOUT?'))
        SpeedWIND = str(sendUDP('SpeedWIND?'))
        HummSOIL = str(sendUDP('HummSOIL?'))
        LightOUT = str(sendUDP('LightOUT?'))
        with open("SharedData.txt", "w+") as f:
            f.write(f"D2;{DI[0]};\n")
            f.write(f"D3;{DI[1]};\n")
            f.write(f"D4;{DI[2]};\n")
            f.write(f"D5;{DI[3]};\n")
            f.write(f"D6;{DI[4]};\n")
            f.write(f"D7;{DI[5]};\n")
            f.write(f"D16;{DI[6]};\n")
            f.write(f"D17;{DI[7]};\n")
            f.write(f"D26;{DI[8]};\n")
            f.write(f"D27;{DI[9]};\n")
            f.write(f"D36;{DI[10]};\n")

            f.write(f"D28;{DO[0]};\n")
            f.write(f"D29;{DO[1]};\n")
            f.write(f"D30;{DO[2]};\n")
            f.write(f"D31;{DO[3]};\n")
            f.write(f"D32;{DO[4]};\n")
            f.write(f"D33;{DO[5]};\n")
            f.write(f"D34;{DO[6]};\n")
            f.write(f"D35;{DO[7]};\n")
            f.write(f"D37;{DO[8]};\n")
            f.write(f"D38;{DO[9]};\n")
            f.write(f"D39;{DO[10]};\n")
            f.write(f"D40;{DO[11]};\n")
            f.write(f"D41;{DO[12]};\n")
            f.write(f"D42;{DO[13]};\n")
            f.write(f"D43;{DO[14]};\n")
            f.write(f"D44;{DO[15]};\n")

            f.write(f"TempOUT;{TempOUT};\n")
            f.write(f"HummOUT;{HummOUT};\n")
            f.write(f"SpeedWIND;{SpeedWIND};\n")
            f.write(f"HummSOIL;{HummSOIL};\n")
            f.write(f"LightOUT;{LightOUT};\n")

        time.sleep(1)
except:
    pass