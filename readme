Below is explaination of game score manager software.

Updates of score manager is based on the message queueing protocol based on zeromq  aka ZMQ
We used published subscriber model of message queuing. There are two types of publishers in this.

First
Players(Pub[2,3,..,N]):
Each player is a publisher which updates the various stats to the serve as and when they happen.

Centeral Server(Pub1):
This publishers is responsible to send updates of the score and other players stats.

Since there are two publishers they have their respective subscriber.
Subscriber at server:
This will listen to all the players as they publish various stats. Use this to update the logger and database for
further processing.

Subscriber at Player:
This will listen to the server publisher for the updates and display it on the screen.

Publishiers (filenames)

pubserver.py
pubp1.py
pubp2.py
..
pubpN.py

Subscribers (filenames)
subp1.py
subp2.py
...
subpN.py

subserver.py


The start sequence
- Start all subscribers
- Start all Publishers
- Test Connectivity.
- Initiate Game (database update)
- Start


