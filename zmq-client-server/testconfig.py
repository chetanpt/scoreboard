__author__ = 'Chetan'
from configparser import ConfigParser
config = ConfigParser(allow_no_value=True)

config.read("D:\\Work\superhuman\\scoreboard\\zmq-client-server\\configuration\\config.ini")
#config.read('config.ini')
dbname = config['Database']['name']
dbuser = config['Database']['user']


print dbname
print dbuser