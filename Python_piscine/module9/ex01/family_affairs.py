#!/usr/bin/env python3
def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name] == "red", family_dict.keys()))
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
    #"dup": "red"
}

print(find_the_redheads(dupont_family))