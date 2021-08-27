class RobotClient():
    def __init__(self, host, port, verbosity):
        self.host = host
        self.port = port
        self.socket_fd = -1
        self.verbosity = verbosity
        self.history_total_size = 0
        self.client_start = 0
        self.last_history_print = 0
