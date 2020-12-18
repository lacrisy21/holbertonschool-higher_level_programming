#!/usr/bin/python3
def uniq_add(my_list=[]):
    seta = set(my_list)
    b = 0
    for a in seta:
        b = a + b
    return(b)
