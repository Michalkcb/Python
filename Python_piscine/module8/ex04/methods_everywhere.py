#!/usr/bin/env python3
import sys

def shrink(input_string):
    print(input_string[:8])

def enlarge(input_string):
    while len(input_string) < 8:
        input_string += 'Z'
    print(input_string)

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)