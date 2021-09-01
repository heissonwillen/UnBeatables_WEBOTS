import socket
import time
import struct
import messages_pb2
from google.protobuf import text_format


class RobotClient():
    history_period = 5
    # Adding some margin for other data than image
    max_answer_size = 1920 * 1080 * 3 + 1000
    max_attempts = 20
    wait_time_sec = 1

    def __init__(self, host=None, port=None, verbosity=None):
        self.host = host
        self.port = port
        self.socket_fd = -1
        self.verbosity = verbosity
        self.history_total_size = 0
        self.client_start = 0
        self.last_history_print = 0

    def connect_client(self):
        server = socket.gethostbyname(self.host)
        self.socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.socket_fd == -1:
            if self.verbosity > 0:
                print("Cannot create socket")
            return False

        connected = False
        for attempt in range(1, RobotClient.max_attempts+1):
            try:
                self.socket_fd.connect((server, self.port))
                connected = True
                break
            except Exception:
                print(
                    f"Failed to connect to {self.host}:{self.port} (attempt {attempt} / {RobotClient.max_attempts})")
                time.sleep(RobotClient.wait_time_sec)

        if not connected:
            if self.verbosity > 0:
                print(
                    f"Failed to connect after {attempt} attempts. Giving up on connection")
                self.disconnect_client()
            return False

        answer = self.socket_fd.recv(8).decode("utf-8")
        if self.verbosity >= 4:
            print(f"Welcome message: {answer}")
        if answer != "Welcome\0":
            if self.verbosity > 0:
                if answer == "Refused\0":
                    print(
                        f"Connection to {self.host}:{self.port} refused: your IP address is not allowed in the game.json configuration file.")
                else:
                    print(f"Received unknown answer from server: {answer}")
            self.disconnect_client()
            return False
        if self.verbosity >= 2:
            print(f"Connected to {self.host}:{self.port}")
        return True

    def disconnect_client(self):
        if self.socket_fd == -1 and self.verbosity > 0:
            print("RobotClient is already disconnected")
            return
        self.socket_fd.close()
        self.socket_fd = -1

    def send_request(self, actuator_request):
        if self.socket_fd == -1:
            raise Exception("RobotClient is not connected")

        # Need refactoring
        try:
            size = struct.pack(">L", len(actuator_request))
            self.socket_fd.send(size + actuator_request)
        except:
            self.disconnect_client()

    def is_ok(self):
        return self.socket_fd != -1

    def receive(self):
        size = self.socket_fd.recv(4)
        size = struct.unpack(">L", size)[0]

        answer = bytearray()
        while len(answer) < size:
            packet = self.socket_fd.recv(size - len(answer))
            if not packet:
                return None
            answer.extend(packet)

        sensor_measurements = messages_pb2.SensorMeasurements()
        sensor_measurements.ParseFromString(answer)

        if self.verbosity >= 2:
            # print messages
            pass
        if self.verbosity >= 3:
            # update history
            pass
        if self.verbosity >= 4:
            # print sensor measurements
            pass

        return sensor_measurements

    def update_history(self):
        pass

    def build_request_message(self, path=""):
        with open(path, "rb") as fd:
            actuator_request = messages_pb2.ActuatorRequests()
            text_format.Parse(fd.read(), actuator_request)

        return actuator_request.SerializeToString()
