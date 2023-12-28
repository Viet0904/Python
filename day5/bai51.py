# for , while
# for ở trong Python có tác dụng lặp các biến dữ liệu có trong list , tuple hoặc string,... Sử dụng cú pháp như sau:
# for variable in data:
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
name = "Viet"
for char in name:
    print(char)
for number in range(1,11,3):
    print(number)
sum = 0
for number in range(1,101):
    sum+=number
print(sum)