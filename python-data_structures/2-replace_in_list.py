#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list[3] = 9
    idx = element
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        return my_list[idx]