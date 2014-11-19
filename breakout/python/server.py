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
            print("Client %s: %s" % (str(id), str(data)))
        except serror:
            print("Client %s: left" % id)
            conn.close()
            break

while True:
    print("<<<<<<<<<<<<<<<<<<<< No of clients: %s >>>>>>>>>>>>>>>>>>>>" %
          len(clients))
    try:
        conn, addr = sock.accept()
        clients.append(addr)
        print("Client %i: joined!" % clients.index(addr))
        start_new_thread(clientthread, (conn, clients.index(addr)))
    except KeyboardInterrupt:
        conn.close()
        sock.close()
