#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start < end:
        result = list(range(start, end + 1))
    else:
        result = list(range(start, end - 1, -1))

    print(result)