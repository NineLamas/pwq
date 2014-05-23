#!/usr/bin/python
#Simple Server

import socket,sys

host = ''
port = 55055

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." % port

clientsock,addr = s.accept()
recvfromclientbuf = clientsock.recv(2048)
if 0 < len(recvfromclientbuf):
    sys.stdout.write(recvfromclientbuf)
    print "Client IP is:", addr
    replymessage = "HI, I am Server!!! \r\n"
    clientsock.send(replymessage)

clientsock.close()
s.close() 
