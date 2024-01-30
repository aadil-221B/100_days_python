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
def check_resources(prompt):
    for key in MENU[prompt]["ingredients"]:
        if MENU[prompt]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def check_money(prompt):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total >= MENU[prompt]["cost"]:
        change = total - MENU[prompt]["cost"]
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(prompt):
    for key in MENU[prompt]["ingredients"]:
        resources[key] -= MENU[prompt]["ingredients"][key]
    print(f"Here is your {prompt}. Enjoy!")
def coffee_machine():
    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt == "off":
            break
        elif prompt == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
        elif check_resources(prompt) and check_money(prompt):
            make_coffee(prompt)
coffee_machine()

