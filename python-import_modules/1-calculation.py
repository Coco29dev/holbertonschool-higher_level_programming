#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    resultat = add(a, b)
    print("{} + {} = {}".format(a, b, resultat))
    resultat = sub(a, b)
    print("{} - {} = {}".format(a, b, resultat))
    resultat = mul(a, b)
    print("{} * {} = {}".format(a, b, resultat))
    resultat = div(a, b)
    print("{} / {} = {}".format(a, b, resultat))
