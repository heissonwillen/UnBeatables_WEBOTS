import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    for arg_idx, current_arg in enumerate(args):
        if current_arg[0] == '-':
            if current_arg == '-v':
                if arg_idx + 1 >= len(args):
                    print("Missing value for verbosity")
