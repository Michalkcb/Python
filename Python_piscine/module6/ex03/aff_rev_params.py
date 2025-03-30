#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)