rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice = [0,1,2]
user_choice = int(input("What do you chose? Type 0 for Rock,1 for Paper or 2 for scissors "))
computer_choice = random.choice(choice)
print("You chose:")

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == user_choice:
    print("Draw")
elif user_choice ==0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You Win")
elif user_choice == 1:
    if computer_choice ==2:
        print("You Lose")
    elif computer_choice ==0:
        print("You Win")
elif user_choice == 2:
    if computer_choice ==1:
        print("You Win")
    elif computer_choice == 0:
        print("You Lose")

