#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
 
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    ile = text.count(keyword)

    if ile > 0:
        print(ile)
    else:
        print("none") 