#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    s_copy = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            s_copy[count] = True
        else:
            s_copy[count] = False
    return(s_copy)
