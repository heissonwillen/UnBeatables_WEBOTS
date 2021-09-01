import messages_pb2


actuator_request = messages_pb2.ActuatorRequests()
with open("my_request.txt", "wb") as fd:
    actuator_request.motor_positions("test", 1)
    fd.write(actuator_request)

# print(text_format.Parse(s, actuator_request.ActuatorRequests()))
