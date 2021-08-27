import socket

import time

PORT = 10002
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

if client == -1:
    print("Cannot create socket")

client.connect(ADDR)
print(client.recv(2048).decode(FORMAT))

time.sleep(10)