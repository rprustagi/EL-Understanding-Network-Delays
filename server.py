#!/usr/bin/python
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvr_addr = ('10.1.1.1', 9997)

sock.bind(srvr_addr)

while True:
    data, addr = sock.recvfrom(2000)
    if data:
        time.sleep(.010) #srv proc time
        sent = sock.sendto(data, addr)



