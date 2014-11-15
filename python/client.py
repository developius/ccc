#!usr/bin/python
from socket import *
import time
from socket import error as serror

host = 'localhost'
port = 42000

def connect():
	global irc
	irc = socket(AF_INET, SOCK_STREAM)
	irc.connect((host, port))

connect()
while True:
	try:
		data = irc.recv(4096)
		irc.send('Hi! I am client %s.' % data)
		print("I am client %s as told by server" % data)
	except serror:
		print ("Server offline :(")
	time.sleep(5)