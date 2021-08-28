import socket
import time


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
        socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if not socket_fd:
            if self.verbosity > 0:
                print("Cannot create socket")
            return False

        connected = False
        for attempt in range(1, RobotClient.max_attempts+1):
            try:
                socket_fd.connect((server, self.port))
                connected = True
                break
            except Exception:
                print(
                    f"Failed to connect to {self.host}:{self.port} (attempt {attempt} / {RobotClient.max_attempts})")
                time.sleep(RobotClient.wait_time_sec)

        if not connected:
            if self.verbosity > 0:
                print(
                    "Failed to connect after {attempt} attempts. Giving up on connection")
                socket_fd.close()
            return False

        answer = socket_fd.recv(8).decode("utf-8")
        if self.verbosity >= 4:
            print("Welcome message: {answer}")
        if not "Welcome" in answer:
            if self.verbosity > 0:
                if "Refused" in answer:
                    print(
                        f"Connection to {self.host}:{self.port} refused: your IP address is not allowed in the game.json configuration file.")
                else:
                    print(f"Received unknown answer from server: {answer}")
            socket_fd.close()
            return False
        if self.verbosity >= 2:
            print(f"Connected to {self.host}:{self.port}")
        return True

    # def disconnect_client(self):
    #     try:
    #         socket_fd.close()
    #     except Exception:
    #         print("RobotClient is already disconnected")

    def send_request(self):
        pass

    def is_ok(self):
        pass

    def receive_data(self):
        pass

    def update_history(self):
        pass
