#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print(f"{num_args}", end=' ')

    if num_args == 0:
        print("arguments.")
    elif num_args == 1:
        print("argument:")
        print(f"{1}: {args[0]}")
    else:
        print("arguments:")

        for i in range(num_args):
            print(f"{i + 1} : {args[i]}")
        """for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")"""
