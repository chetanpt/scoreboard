__author__ = 'Chetan'
import time
from scoremanager import serverside

servercontext = serverside()
conn = servercontext.connectdb()

cur = conn.cursor()

cur.execute("select *  from game.player;")
id, name = cur.fetchone()

print id
print name