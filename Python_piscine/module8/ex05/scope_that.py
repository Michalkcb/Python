#!/usr/bin/env python3

def add_one(number):
    return number + 1

my_variable = 5
print(f"Before calling add_one: {my_variable}")

my_variable = add_one(my_variable)

print(f"After calling add_one: {my_variable}")
