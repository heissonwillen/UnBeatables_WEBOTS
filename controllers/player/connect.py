import socket
import time

HEADER = 64
PORT = 10002
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "localhost"

socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket_fd)

socket_fd.connect((SERVER, PORT))


# def send(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER - len(send_length))
#     socket_fd.send(send_length)
#     socket_fd.send(message)
#     print(socket_fd.recv(2048).decode(FORMAT))


# send("Hello World!")
# input()
# send("Hello Everyone!")
# input()
# send("Hello Tim!")

# send(DISCONNECT_MESSAGE)

print(socket_fd.recv(2048).decode(FORMAT))
time.sleep(3)
