from socket import socket,AF_INET,SOCK_STREAM
import sys

  
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
fname = sys.argv[0]
img = open(fname,'rb')
BUFFER_SIZE = len(img.read())  # Normally 1024, but we want fast response
 
s = socket(AF_INET,SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while True:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	conn.send(data)  # echo
conn.close()

