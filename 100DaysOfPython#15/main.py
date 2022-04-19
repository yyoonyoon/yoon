from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

About_Menu = Menu()
About_Payment = MoneyMachine()
About_CoffeeMaker = CoffeeMaker()
is_on = True

while is_on:
    print(About_Menu.get_items())
    order_name = input("Please select the menu you want. : ").lower()
    if order_name == "off":
        break
    elif order_name == "report":
        About_CoffeeMaker.report()
        About_Payment.report()
        break
    else :
        About_Menu.find_drink(order_name)

    if(order_name == "latte"):
        order_name = About_Menu.menu[0]
    elif(order_name == "espresso"):
        order_name = About_Menu.menu[1]
    elif(order_name == "cappuccino"):
        order_name = About_Menu.menu[2]
    About_CoffeeMaker.is_resource_sufficient(drink= order_name )

    About_Payment.make_payment(cost= order_name.cost)
    About_CoffeeMaker.make_coffee(order= order_name)
    print("\n")