import socket
import sys
import struct
import time
import binascii
 
host = '192.168.100.100'
port = 9004
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
inputHex = binascii.unhexlify("4C4F4E0D") #sent command start QR Code Reader 
try:
    s.connect((host, port))
    print('connect tcp')
    s.send(inputHex)
    time.sleep(1)
except socket.gaierror:
    print('Hostname could not be resolved Exiting')

print('Socket connected to ' + host + ' on ip ')
try:
    while True:
        data = s.recv(1024) 
        if not data:
            print("read fail")
        print(data)

except socket.error:
    print('send fail')
    sys.exit()