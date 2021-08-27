import socket


class RobotClient():
    def __init__(self, host=None, port=None, verbosity=None):
        self.host = host
        self.port = port
        self.socket_fd = -1
        self.verbosity = verbosity
        self.history_total_size = 0
        self.client_start = 0
        self.last_history_print = 0

    def connect_client(self):
        print(self.host)
        server = socket.gethostbyname(self.host)
        print(server)
        pass

    def disconnect_client(self):
        pass

    def send_request(self):
        pass

    def is_ok(self):
        pass

    def receive_data(self):
        pass

    def update_history(self):
        pass
