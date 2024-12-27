from .data import MENU, resources, profit
from common_functions import typing, hold_screen, clear_screen, get_input

def print_report():
    typing(f"Water: {resources['water']}ml \n")
    typing(f"Milk: {resources['milk']}ml \n")
    typing(f"Coffee: {resources['coffee']}g \n")
    typing(f"Money: ${profit} \n")

def is_resource_sufficient(ingredients, resources):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            typing(f"Sorry there is not enough {item}.\n")
            return False
    return True

def insert_coint():
    typing("Insert the Coins...\n")
    total = get_input("Quarters: ",is_int=True) * 0.25
    total += get_input("Dimes : ",is_int=True) * 0.10
    total += get_input("Nickles : ", is_int=True) * 0.05
    total += get_input("Pennies : ", is_int=True) * 0.01
    return round(total,2)

def is_transaction_successful(recieved, cost):
    if recieved > cost:
        change = round(recieved - cost, 2)
        typing(f"Here is your Change : {change}\n")
        global profit
        profit += cost
        return True
    else:
        typing(f"Required :{cost} Provided : {recieved}\nSorry that's not enough money. Money refunded.\n")
        return False

def make_coffee(choice, ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    typing(f"Enjoy your {choice} ☕ \n")
    
clear_screen()
typing("Welcome to the Coffee Machine!\n")
hold_screen()
while True: 
    clear_screen()
    choice = get_input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == 'off':
        break
    elif choice == 'report':
        print_report()
        hold_screen()
    else:
        if choice in MENU:
            drink = MENU[choice]
            ingredients = drink['ingredients']
            cost = drink['cost']
            if is_resource_sufficient(ingredients, resources):
                typing(f"Please Provide : ${cost}\n")
                total = insert_coint()
                if is_transaction_successful(total, cost):
                    make_coffee(choice, ingredients)
            hold_screen()
        else:
            typing("Enter Valid Input!\n")
            hold_screen()

