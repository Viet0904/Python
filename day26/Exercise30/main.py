file1 = open("day26/Exercise30/file1.txt", mode="r")
data1 = [line.strip() for line in file1.readlines()]
file2 = open("day26/Exercise30/file2.txt", mode="r")
data2 = [line.strip() for line in file2.readlines()]


result = [int(number) for number in data1 if number in data2]


# Write your code above 👆
print(result)
