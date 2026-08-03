# Day 16 - Coffee Maker 2.0
# Using Object Oriented Programming (OOP) to update the Coffee maker form day 15

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

coffee_on = True
while coffee_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        coffee_on = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        menu_item_ordered = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(menu_item_ordered) and money_machine.make_payment(menu_item_ordered.cost):
            coffee_machine.make_coffee(menu_item_ordered)
