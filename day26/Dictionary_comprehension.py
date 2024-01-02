# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_score = {student: random.randint(1, 100) for student in names}
passed_student = {key: value for (key, value) in student_score.items() if value >= 60}

print(passed_student)
