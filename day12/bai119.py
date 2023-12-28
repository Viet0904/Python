#Modifying Global Scope
enemies = 1 #Global scope
def increase_enemies():
    global enemies 
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies inside function: {enemies}")

#Gloabal Constant : Hằng số viết Hoa
 
PI= 3.14
URL = "https://www.google.com"