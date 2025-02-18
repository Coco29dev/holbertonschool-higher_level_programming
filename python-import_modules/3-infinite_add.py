#!/usr/bin/python3
import sys

if __name__ == "__main__":
    resultat = 0

    for i in range(1, len(sys.argv)):
        resultat += int(sys.argv[i])
    print("{}".format(resultat))
