import time
import messages_pb2
from google.protobuf import text_format
import socket
import struct


actuator_request = messages_pb2.ActuatorRequests()
with open("actuator_requests.txt", "rb") as fd:
    s = fd.read()
    text_format.Parse(s, actuator_request)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10001        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    msg = actuator_request.SerializeToString()
    msg_size = struct.pack(">L", len(msg))

    s.send(msg_size + msg)

    data = s.recv(1024)

    time.sleep(2)

    s.close()

# print(text_format.Parse(s, actuator_request.ActuatorRequests()))
