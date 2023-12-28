import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
# Function to clear the console
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
print(logo)
print("Wellcom to the secret auction program.")
loop = True
auctioneers = []
while loop:
    name = input("What is your name?: ")
    auction_price = float(input("What's your bid?: $"))
    temp = {}
    temp[name] = auction_price;
    auctioneers.append(temp)
    again = input("Are there any other bidders? Type 'yes' or 'no. ").lower()
    if again == "yes":
        clear()
        loop = True
    else:
        loop = False

def findMax(a,b):
    return a if a>b else b

price_winner = 0
user_winner = ""
max= -1;
for item in auctioneers:
    for key,val in item.items():
        if val > max:
            max = val
            user_winner = key
            price_winner = val

print(f"The winner is {user_winner} with a bid of ${price_winner}")
