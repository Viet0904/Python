student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# for key, value in student_dict.items():
#     print(value)
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Lặp với data frame
# for key, value in student_data_frame.items():
#     print(value)

# Lặp qua mỗi dòng của data frame
for index, row in student_data_frame.iterrows():
    # print(row.student)
    if row.student == "Angela":
        print(row.score)
