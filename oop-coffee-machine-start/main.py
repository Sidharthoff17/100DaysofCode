from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
def user_order() -> str:
    while True:
        try:
            coffeeType = input("What is your order(espresso/latte/cappuccino):").strip()
            if coffeeType in ["espresso", "latte", "cappuccino", "off", "report"]:
                break
            raise ValueError
        except ValueError:
            pass

    return coffeeType

def main():
    #create cafe menu object
    cafe_menu = Menu()
    cafe_money_machine = MoneyMachine()
    cafe_coffee_maker = CoffeeMaker()

    #get the drink that is being ordered
    while True:
        #get cafe order
        drink_order = user_order()

        if drink_order == "off":
            break
        elif drink_order == "report":
            cafe_coffee_maker.report()
            cafe_money_machine.report()
        else:
            drink = cafe_menu.find_drink(drink_order)

            #set checkers
            ingredients_checker = cafe_coffee_maker.is_resource_sufficient(drink)
            if not ingredients_checker:
                break
            money_checker = cafe_money_machine.make_payment(drink.cost)
            if not money_checker:
                break

            if money_checker and ingredients_checker:
                cafe_coffee_maker.make_coffee(drink)



main()

