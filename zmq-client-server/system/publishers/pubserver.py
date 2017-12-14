__author__ = 'Chetan'
import sys
sys.path.append('D:\Work\superhuman\scoreboard\zmq client-server')
from publisher import publisher


t1p1 = publisher("team1","player1","T1P1",'localhost',7001)
t2p1 = publisher("team2","player1","T2P1","localhost",7002)

print t1p1.team, t2p1.team
print t2p1.team, t2p1.team

t1p1.configure()
t1p1.startpub()

