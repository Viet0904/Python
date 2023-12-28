#Number Guessing Game Objectives:
from art import logo
import random
import os
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
dict_count = {"easy":10,"hard":5}
loop = True
while loop:
    number = random.randint(1,100)
    print(number)
    print(logo)
    print("Wellcome to the Number Guessing game")
    print("I'm thinking of a number between 1 and 100.")
    chose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    count = dict_count[chose]
    while count >0:
        print(f"You have {count} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        count -=1
        if guess == number:
            print(f"You got it! The answer was {number}")
            break
        elif guess > number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
    if count ==0:
        print("You've run out of guesses, you lose. ")
    again = input("Do you want to play again. Type 'y' or 'n': ").lower()
    if again == 'y':
        clear()
    else:
        loop = False



# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
