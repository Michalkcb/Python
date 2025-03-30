#!/usr/bin/env python3
table = 0

while table <= 10:

    multiplier = 0
    
    print(f"Table of {table}:", end=" ")

    while multiplier <= 10:
        print(table * multiplier, end=" ")
        multiplier += 1

    print()

    table += 1