from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

obj_menu = Menu()
obj_money_machine = MoneyMachine()
obj_coffe_maker = CoffeeMaker()
is_on = True
while is_on:
    choice = input(f"What would you like? ({obj_menu.get_items()}) : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        obj_coffe_maker.report()
        obj_money_machine.report()
    else:
        if obj_menu.find_drink(choice):
            drink = obj_menu.find_drink(choice)
            if obj_coffe_maker.is_resource_sufficient(drink):
                if obj_money_machine.make_payment(drink.cost):
                    obj_coffe_maker.make_coffee(drink)