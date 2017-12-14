__author__ = 'Chetan'
import time
from scoremanager import databasehelper

servercontext = databasehelper()
conn = servercontext.getDbHandle()
servercontext.getData()

#cur = conn.cursor()
#cur.execute("select *  from game.player;")
#id, name = cur.fetchone()
#print id
#print name