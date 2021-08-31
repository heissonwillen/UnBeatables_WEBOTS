import messages_pb2
from google.protobuf import text_format


actuator_request = messages_pb2.ActuatorRequests()
with open("actuator_requests.txt", "rb") as fd:
    # s = fd.read()
    s = b'motor_positions{name:"Neck"}'
    actuator_request.ParseFromString(s)
    print(actuator_request)
    # print(text_format.Parse(fd.read(), actuator_request.ActuatorRequests()))

# print(text_format.Parse(s, actuator_request.ActuatorRequests()))
