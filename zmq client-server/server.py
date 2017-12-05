__author__ = 'Chetan'

import sys
from publisher import publisher

t1p1 = publisher("team1","player1","T1P1",'192.168.200.10',5001)
t2p1 = publisher("team2","player1","T2P1","localhost",5002)

print t1p1.team, t2p1.team

t1p1.configure()
t1p1.startpub()
for line in sys.stdin:
    topic, message = line.split()
    #t1p1.publishMessage("T1P1","Score:10")
    t1p1.publishMessage(topic, message)