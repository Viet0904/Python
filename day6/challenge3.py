#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
count_wrong = 0
while "_" in display:
    if count_wrong == 6:
        break
    guess = input("Guess a letter: ").lower()
    Check = True
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            Check = False
            display[position] = letter
    if Check == True:
        count_wrong +=1
    print(display)
if count_wrong!=6:
    print("You Win")
else:
    print("You Lose")

