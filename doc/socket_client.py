#!/usr/bin/python
#Simple Client

import socket, sys

port = 55055
#host = sys.argv[1]
host = '192.168.11.185'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect( (host, port) )
except socket.gaierror, e:
    print "Error connecting to server: %s" % e
    sys.exit(1)

s.send("Hello, Server !!!\r\n")
buf = s.recv(2048)
if not len(buf):
    s.close()
    sys.exit(1)
sys.stdout.write(buf)

s.close()
