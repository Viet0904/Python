import os
from art import logo
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
def add(a,b):
    return a+b
def multiple(a,b):
    return a*b
def divide (a,b):
    return a/b
def subtract(a,b):
    return a-b
dictionary_operator = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" :divide,
}
def calculator():
    print (logo)
    first_number = float(input("What's the first number?: "))
    for symbol in dictionary_operator:
        print(symbol)
    loop = True
    while loop:
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        total = 0
        total +=dictionary_operator[operator](first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {total}")
        chose = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
        if chose == "y":
            first_number = total
        else:
            clear()
            calculator()

calculator()