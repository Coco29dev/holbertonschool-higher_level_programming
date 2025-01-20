#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Compléter les tuples pour qu'ils aient au moins 2 éléments
    tuple_a = tuple_a + (0, 0)  # Complète tuple_a avec 0 si nécessaire
    tuple_b = tuple_b + (0, 0)  # Complète tuple_b avec 0 si nécessaire

    # Prendre seulement les 2 premiers éléments de chaque tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Additionner les éléments correspondants
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
