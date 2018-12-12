import socket
import sys


def socket_create():
    try:
        global host
        global port
        global s

        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


#Bind socket data to port and wait for connection to client

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:" + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket bonding error" + str(msg) + "\n" + "Retrying")
        socket_bind()

#Establish a connection with client (socket must be listening for them)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP" + address[0] + "| port" + str(address[1])
    send_comands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()