#!/usr/bin/python
from socket import *
from thread import *
from socket import error as serror

host = ''
port = 42000
 
sock = socket()
sock.bind((host, port))
sock.listen(5)

clients = list()

def clientthread(conn, id):
	while True:
		try:
			conn.send(str(id))
			data = conn.recv(1024)
			print(data)
		except serror:
			print("Client %s left" % id)
			conn.close()

while True:
    conn, addr = sock.accept()
    clients.append(addr)
    print("Client %i just joined!" % clients.index(addr))
    start_new_thread(clientthread,(conn,clients.index(addr)))

conn.close()
sock.close()