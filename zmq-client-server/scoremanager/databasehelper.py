__author__ = 'Chetan'
# This class implements database helpers modules
# e.g.
# 1. connect adn disconnect the db
# 2. retrive data from db
# 3. Update database in realtime
# 4. etc...
import time
import psycopg2
import configparser


class databasehelper(object):
# On class initialization it connects to the database defined in config files i.e. configuration/config.ini
    def __int__(self):
        config = configparser.ConfigParser()
        config.read("D:\work\superhuman\scoreboard\zmq-client-server\configuration\config.ini")
        self.dbname = config['Database']['name']
        self.dbuser = config['Database']['user']
        self.conn

    def getDbname(self):
        return "paintball"
    def getDbuser(self):
        return "postgres"

    def getDbHandle(self):
        self.conn = psycopg2.connect("dbname=paintball user=postgres")
        return self.conn

    # Below are methods for Creating Team and Adding players to the team
    def getData(self):
        # This is just a test method and does not means much.
        cur = self.conn.cursor()
        cur.execute("select *  from game.player;")
        id, name = cur.fetchone()
        print id
        print name

    def createTeam(self, teamname):
        self.teamname = teamname

