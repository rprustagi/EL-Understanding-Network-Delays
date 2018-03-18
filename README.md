# EL-Understanding-Network-Delays
Exercises to understand various components of network delays. 
Two programs are described here. One is client side and other is
server side.

**client.py**\
This python program connects to UDP server 10.1.1.1 on port 9997.
For your setup, change these values accordingly.

**server.py**\
This server program receives the UDP message on the specified port
e.g. 9997 and responds back with the same message as received i.e.
echoes back the content. To simulate the processing and queuing
delay, an artificial sleep value (time.sleep(0.010)) corresponding
to 10ms has been introduced. To experiment with various delay
values, change this value to as desired.


