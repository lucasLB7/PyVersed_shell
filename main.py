


#
# def get_data(barf, *doggies, **properties):
#     print(barf, doggies, properties)
#
# get_data('google', 'python', 'flask', 'django', limit = 10, verbose = True, hello = True)


import os
import sys
import socket

def Main():
    host = '127.0.0.1'
    port = 5100

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    print("connection from:" + str(addr))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user:" + str(data))
        data = str(data).upper()
        print("Sending: " + str(data))
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()
