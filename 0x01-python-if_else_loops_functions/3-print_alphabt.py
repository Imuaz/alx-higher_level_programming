#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i == 'q' or i == 'e':
       break
    print("{:c}".format(i), end="")
