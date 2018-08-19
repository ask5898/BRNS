import socket
import time
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
fname = "index.jpeg"
img = open(fname,'rb')
data = bytearray(img.read())
BUFFER_SIZE = len(img.read())
t0=time.time()
s.send(data)
data = s.recv(BUFFER_SIZE)
s.close()
t = time.time()
print(t-t0)
print "received data:",data
