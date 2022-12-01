#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    elenum = len(sys.argv) - 1
    if elenum == 0:
        print("{:d} arguments.".format(elenum))
    elif elenum == 1:
        print("{:d} argument:".format(elenum))
    else:
        print("{:d} arguments:".format(elenum))
    for i in range(elenum):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
