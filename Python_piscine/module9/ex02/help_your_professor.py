#!/usr/bin/env python3
def average(students_scores):
    total_score = sum(students_scores.values())
    
    number_of_students = len(students_scores)
    
    avg = total_score / number_of_students
    
    return avg
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9,
   # "aaa": 5
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")