#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print(0)
    else:
        result = sum(int(arg) for arg in args)
        print(result)
