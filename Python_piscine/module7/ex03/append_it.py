#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
    
else:
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(param + "ism")
    