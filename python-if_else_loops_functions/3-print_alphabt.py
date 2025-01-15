#!/usr/bin/python3
for alph in range(97, 123):
    if alph in [101, 113]:
        continue
    print("{}".format(chr(alph)), end="")
