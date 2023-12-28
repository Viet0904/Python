from art import logo,vs
import random
from game_data import data
import os
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_random_account():
    """Get data from random account"""
    return random.choice(data)
def check_answer(guess,a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def format_data(account):
    return f"{account['name']}, {account['description']} , {account['country']}"
def higher_lower_game():
    print(logo)
    count_correct = 0
    loop = True 
    guess = ''
    account_a = get_random_account()
    account_b = get_random_account()
    while loop:
        account_a = account_b if guess == 'b' else account_a
        account_b = get_random_account()
        while account_a==account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against account_b: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess,account_a['follower_count'],account_b['follower_count'])
        clear()
        print(logo)
        if is_correct:
            count_correct +=1
            print(f"You're right! Current score: {count_correct}.")
        else:
            loop = False
            print(f"Sorry, that's wrong. Final score: {count_correct}")

higher_lower_game()
        

