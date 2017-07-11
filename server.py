import socket
import sys

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
	s.bind((HOST, PORT))
except socket.error:
	print('Bind failed.')
	sys.exit()

print("socket bind successful")
s.listen(10)
print('Socket now listening')
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024)
    reply = b'OK...' + data
    if not data:
        break
    conn.sendall(reply)

conn.close()
s.close()
