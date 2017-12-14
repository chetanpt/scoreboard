__author__ = 'Chetan'
import zmq

class subscriber(object):
     def __init__(self,team,player,topic,ip,port,topicfilter):
        self.team = team
        self.player = player
        self.topic = topic
        self.ip = ip
        self.port = port
        self.topicFilter = topicfilter

     def configure(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)

     def subscribeToTopic(self,topic):
        self.socket.setsockopt(zmq.SUBSCRIBE, topic)

     def startsub(self):
         self.socket.connect("tcp://localhost:%s" % self.port)

     def getMessage(self):
        string = self.socket.recv()
        topic, message = string.split()
        return topic, message