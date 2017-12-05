__author__ = 'Chetan'
from subscriber import subscriber

sub1 = subscriber("team1","Player1","T1P1","localhost",5001,"true")

print sub1.team, sub1.topicFilter
sub1.configure()
sub1.subscribeToTopic("T1P1")
sub1.startsub()

while True:
    topic, message = sub1.getMessage()
    print message
