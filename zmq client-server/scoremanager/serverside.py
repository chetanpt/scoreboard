__author__ = 'Chetan'
import psycopg2
import configparser


class serverside(object):
    def __int__(self):
        self.readconfig()

    def readconfig(self):
        config = configparser.ConfigParser()
        config.read("..\configuration\config.ini")
        self.dbname = config['Database']['name']
        self.dbuser = config['Database']['user']

    def connectdb(self):
        conn = psycopg2.connect("dbname=paintball user=postgres")
        return conn

