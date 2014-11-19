#!/usr/bin/python
from socket import *
from thread import *
from socket import error as serror

host = ''
port = 42000

# setup the server sockets
sock = socket()
sock.bind((host, port))
sock.listen(5)

# example of user data :D
user = {'developius': {'highscore': 10000000, 'loggedIn': False}}


# thread for the clients
def clientthread(conn, username):
    while user[username]['loggedIn']:  # break the thread when user loggs out
        try:
            # 'ping' client (breaks thread on failure)
            conn.send("Just testing that you're awake")
            data = conn.recv(1024)  # get the incomming data - the topscore
            if data:
                # convert data to int for numerical operations
                data = int(data)
                # if we have a highscore...
                if data > user[username]['highscore']:
                    user[username]['highscore'] = data  # ...save it!
        except serror:  # the client is offline
            print("%s left" % username)
            conn.close()
            user[username]['loggedIn'] = False  # stop thread

print("Ready")
while True:
    if user:
        print(
            "<<<<<<<<<<<<<<<<<<<< No of online users: %s >>>>>>>>>>>>>>>>>>>>" % len(user))
        print("SCORES:")
        for name, score in user.iteritems():
            print(" %s: %s" % (name, score['highscore']))
    try:
        conn, addr = sock.accept()
        username = conn.recv(1024)
        if username not in user:  # if new user
            print("New user %s joined" % username)
            conn.send(username)
            user[username] = {'highscore': 0, 'loggedIn': True}
            start_new_thread(clientthread, (conn, username))
        else:  # not a new user
            if not user[username]['loggedIn']:
                # if the user isn't logged in...
                user[username]['loggedIn'] = True  # ...log them in
                start_new_thread(clientthread, (conn, username))

            else:
                # the user is already logged in and we can't have two players with
                # the same name!
                conn.send("username error")
    except KeyboardInterrupt:
        conn.close()
        sock.close()
