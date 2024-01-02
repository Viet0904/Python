# List Comprehension
# Cú pháp new_list =  [new_item for item in list]

# number = [1, 2, 3]
# new_list = [item + 1 for item in number]
# print(new_list)

# name = "Viet"
# new_list = [letter for letter in name]
# print(new_list)

# new_number = [number *2 for number in range(1,5)]
# print(new_number)

# Điều kiện với List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

name_upper = [name.upper() for name in names if len(name) > 5]
print(name_upper)
