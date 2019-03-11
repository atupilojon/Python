
# telnet test

import socket
import traceback

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.settimeout(10)
s.connect(('192.168.2.3',23))

#try:
    #s.connect(('192.168.2.3',23))
#except ConnectionRefusedError:
#    print('Connection refused')

#result = s.recv(4096)

#print(result)
