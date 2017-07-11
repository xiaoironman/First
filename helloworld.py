import sys
import socket

import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket!")
    sys.exit()
print("Socket created!")

host = 'www.oschina.net'
port = 80

try:
	remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print("can't find host address!")
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip , port))
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

message = b"GET / HTTP/1.1\r\n\r\n"
try:
    s.send(message)
except socket.error:
    print("send failed")
    sys.exit()

print("message sent successfully!")

reply = s.recv(4096)
print(reply)
s.close()

#actually a local client for socket applications