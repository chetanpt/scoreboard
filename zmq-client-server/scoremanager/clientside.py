__author__ = 'Chetan'

import psycopg2
from databasehelper import databasehelper

class clientside(object):
    def __init__(self):
        databasehelper.readconfig()
        self.conn = databasehelper.connectdb()
