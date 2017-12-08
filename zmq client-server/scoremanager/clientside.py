__author__ = 'Chetan'

import psycopg2
from serverside import serverside

class clientside(object):
    def __init__(self):
        serverside.readconfig()
        self.conn = serverside.connectdb()
