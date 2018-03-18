#!/usr/bin/python
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvr_addr = ('10.1.1.1', 9997)

sum = 0.0
msg = "Computing Network Delays"
for i in range(1,1000):
    start_time = time.time()
    sent = sock.sendto(msg, srvr_addr)
    data, server = sock.recvfrom(4096)
    end_time = time.time()
    sum = sum + end_time - start_time

#compute resp time for one request
resp_time = sum / 1000

print "Avg. Resp time over 1000 trials = ", resp_time


