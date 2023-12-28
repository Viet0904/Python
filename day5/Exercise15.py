# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height= 0
for height in student_heights:
  total_height +=height
number_student = len(student_heights)
averge_height = round(total_height/ number_student)
print(f"total height = {total_height}")
print(f"number of students = {number_student}")
print(f"average height = {averge_height}")