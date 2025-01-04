from .menu import Menu, MenuItem

from .coffee_maker import CoffeeMaker
from .money_machine import MoneyMachine
from common_functions import typing, hold_screen, clear_screen, get_input

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

clear_screen()
typing("Welcome to Coffee Machine !☕️\n")
hold_screen()
while True:
    clear_screen()
    options = menu.get_items()
    choice = get_input(f"What would you like to have {options} : ").lower()
    if choice == 'off':
        break
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    hold_screen()

