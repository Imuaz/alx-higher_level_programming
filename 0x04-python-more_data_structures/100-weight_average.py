#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    argt = 0
    size = 0

    for x, y in my_list:
        argt += x * y
        size += y

    return (argt / size)
