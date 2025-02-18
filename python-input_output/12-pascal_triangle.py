#!/usr/bin/python3

def pascal_triangle(n):
    if not isinstance(n, int):
        raise TypeError("n n'est pas un int")
    if n <= 0:
        return list(n)
