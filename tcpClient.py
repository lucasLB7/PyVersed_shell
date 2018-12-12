import socket
import subprocess

def Main():
    host = '127.0.0.1'
    port = 5100

    s = socket.socket()
    s.connect((host, port))
    message = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
    while message != "q":
        s.send(message)
        data = s.recv(1024)
        print("Received from server: " + str(data))
        message = raw_input("->")
    s.close()

if __name__ == '__main__':
    Main()
