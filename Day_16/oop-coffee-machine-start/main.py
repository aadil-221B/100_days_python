from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# CoffeeMaker().report()
# MoneyMachine().report()
# drink_name = Menu().find_drink("latte").name
# print(drink_name)
# drink = Menu().find_drink("latte")
# print(CoffeeMaker().is_resource_sufficient(drink))
# print(drink.cost)
# MoneyMachine().make_payment(drink.cost)
# CoffeeMaker().make_coffee(drink)
def main():
    while True:
        options = Menu().get_items()
        prompt = input(f"What would you like? ({options}): ")
        if prompt== "off":
            break
        elif prompt == "report":
            CoffeeMaker().report()
            MoneyMachine().report()
        else:
            drink = Menu().find_drink(prompt)

            if CoffeeMaker().is_resource_sufficient(drink) and MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)
main()