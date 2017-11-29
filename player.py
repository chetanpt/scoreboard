__author__ = 'Chetan'

# player gets hits and updates the hit count on server. This updates the scores on
# opposition player screen and also on the scoreboard.

# passing the message of hit count is done using zeroMq message queues
# Note ( We need to test the speed of these queue in terms of pulling and pushing the messages and how fast it can
# update the scores.

# This file represent a player getting hit and will update the hit count on server.

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket =  context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print msg
    socket.send("Hit 01")
    socket.send("Hit 02")
    time.sleep(1)