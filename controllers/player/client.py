from os import pipe
import sys

from robot_client import *
import numpy as np
import cv2


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

    if port == -1:
        usage("Missing arguments")

    client = RobotClient(host, port, verbosity)
    client.connect_client()

    while client.is_ok():
        try:
            request = client.build_request_message("actuator_requests.txt")
            client.send_request(request)
            sensor_measurements = client.receive()
            for camera in sensor_measurements.cameras:
                img_array = np.frombuffer(camera.image, np.uint8).reshape(
                    camera.height, camera.width, 3)
                cv2.imshow('image', img_array)
                cv2.waitKey(0)
        except Exception as e:
            print(e)
