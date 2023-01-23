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
        time.sleep(1)
except:
    pass
