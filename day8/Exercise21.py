# Write your code below this line 👇
import math
def prime_checker(number):
    if (number ==2):
        print("It's a prime number.")
    elif number <=1: 
        print("It's not a prime number.")
    else:
        check = True
        for i in range(2,int(math.sqrt(number))+1):
            if number % i ==0:
                check=False
        if check == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")





# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)