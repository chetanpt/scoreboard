__author__ = 'Chetan'
import zmq

class publisher(object):
    def __init__(self,team,player,topic,ip,port):
        self.team = team
        self.player = player
        self.topic = [topic]
        self.ip = ip
        self.port = port

    def creteTopic(self,topic):
        if(self.topic.index(topic)):
            print "Topic exists\n"
        else:
            self.topic.append(topic)

    def configure(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)

    def startpub(self):
        print self.ip, self.port
        self.socket.bind("tcp://*:%s" % self.port)

    def publishMessage(self,topic,message):
        self.socket.send("%s %s" % (topic, message))





