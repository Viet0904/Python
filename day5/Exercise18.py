target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
if(target<2):
  total =0
else:
  for number in range(2,target+1,2):
    total+=number
print(total)
