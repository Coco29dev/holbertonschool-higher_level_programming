#!/usr/bin/python3
import sys

if __name__ == "__main__":

    count = len(sys.argv)
    arg = count - 1

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
