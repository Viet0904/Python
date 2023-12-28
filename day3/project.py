print('''
                    _,--.       ,--._
                \  > `-"""-' <  /
                 `-.         .-'
                   / 'e___e` \
                  (   (o o)   )
                  _\_  `='  _/_
                 / /|`-._.-'|\ \
                / /||_______||\ \
              _/ /_||=======||_\ \_
             / _/==||       ||==\_ \
             `'(   ^^       ^^   )`'
                \               /
                 \______|______/ hjw
                 |______|______|
                   )__|   |__(
                  /   ]   [   \
                  `--'     `--'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
lr = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"? ").lower()
if lr == "left":
    sw = input("Swim or wait ").lower()
    if sw =="wait":
        door = input("Red or Blue or Yellow ").lower()
        if door=="yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire.Game Over.")
        elif door=="blue":
            print("Eaten by beasts.Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("You fell nto a hole. Game over")