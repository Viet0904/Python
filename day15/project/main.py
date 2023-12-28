MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money= 0
def give_money():
    total = 0
    print("Please insert coins.")
    total += round (float(input("How many quarters?: "))*0.25,2)
    total+= round (float(input("How many dimes?: "))*0.1,2)
    total+= round (float(input("How many nickles?: "))*0.05,2)
    total+= round (float(input("How many pennies?: "))*0.01,2)
    return total

def check_resources(choice):
    for val in choice:
        if resources[val] < choice[val]:
            print(f"Sorry there is not enough {val}")
            return False
    return True

    
is_on = True
while is_on:
    choose_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_drink == "off":
        is_on = False
    elif choose_drink == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    else:
        drink = MENU[choose_drink]
        pay_ment = drink['cost']
        if check_resources(drink["ingredients"]):
            receive_money = give_money()
            if pay_ment <= receive_money:
                money += pay_ment
                money = round(money,2) 
                for val in drink["ingredients"]:
                    resources[val] -= drink["ingredients"][val]
                print(f"Here is ${round(receive_money-pay_ment,2)} in change.")
                print(f"Here is your {choose_drink} day.")
            else:
                print(f"Sorry that's not enough money. Money refunded")
        
        
