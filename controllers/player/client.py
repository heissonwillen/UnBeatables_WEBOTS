import sys

from robot_client import *


def usage(error_msg=None):
    if error_msg:
        print("Invalid call: " + error_msg, file=sys.stderr)
    print("Usage: client [-v verbosity_level] <host> <port>", file=sys.stderr)


if __name__ == '__main__':
    args = sys.argv[1:]

    port = -1
    verbosity = 3
    host = ''
    for arg_idx, current_arg in enumerate(args):
        # Treating arguments
        if current_arg[0] == "-":
            if current_arg == "-v":
                if arg_idx + 1 >= len(args):
                    print("Missing value for verbosity")
                verbosity = int(args[arg_idx + 1])
            else:
                # current_arg == "-h" or "--help" or anything else
                usage()

        elif len(host) == 0:
            host = current_arg
        elif port == -1:
            port = int(current_arg)
            if port < 0:
                usage("Unexpected negative value for port: " + current_arg)
        else:
            usage("Unexpected additional argument: " + current_arg)

    if (port == -1):
        usage("Missing arguments")

    client = RobotClient(host, port, verbosity)
    client.connect_client()

    print(client.is_ok())
