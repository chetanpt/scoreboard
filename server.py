__author__ = 'Chetan'

# This is a server file and it recieves the message from player when he gets hit. This server is also responsible to
# update the hitter player/team and score board.

# updating can be done using another queue or REST Api as push pull mechanism.

import zmq
import random
import sys
import time
import Tkinter

port = "5556"
print zmq.pyzmq_version()
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send("Any Hit recieved")
    msg = socket.recv()
    print msg
    time.sleep(1)