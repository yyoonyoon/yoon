MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

power = 'on'
profits = 0
is_ok = True

def check_resources(menu):
    global power
    if menu == 'espresso' or menu == 'latte' or menu == 'cappuccino' :
        if MENU[menu]["ingredients"]["water"] > resources["water"]:
            print("Sorry, We don't have enough water.\n")
            power = input("If you turn off the machine, Type 'off' else type 'on': ")
            if (power == 'off'):
                print("Coffee Machine was shutted off.")
            return power
        elif MENU[menu]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, We don't have enough milk.\n")
            power = input("If you turn off the machine, Type 'off' else type 'on': ")
            if (power == 'off'):
                print("Coffee Machine was shutted off.")
            return power
        elif MENU[menu]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, We don't have enough coffee.\n")
            power = input("If you turn off the machine, Type 'off' else type 'on': ")
            if (power == 'off'):
                print("Coffee Machine was shutted off.")
            return power
    else:
        print("You entered wrong menu. Please type agian. \n\n")
        power = input("If you turn off the machine, Type 'off' else type 'on': ")
        if (power == 'off'):
            print("Coffee Machine was shutted off.")
    
def check_money(menu, receieved_quarters, receieved_dimes, receieved_nickles, receieved_pennies):
    global exchange
    global power
    global profits
    global is_ok
    money_input = (0.25 * receieved_quarters) + (0.1 * receieved_dimes)\
        + (0.05 * receieved_nickles) + (0.01 * receieved_pennies)
    if money_input > MENU[menu]["cost"]:
        profits += MENU[menu]["cost"]
        is_ok = True
        report()
        exchange = money_input - MENU[menu]["cost"]
        print("Enjoy your coffee ☕️")
        print("Here is your exchange. : ${0}\n".format(exchange))
        power = input("If you turn off the machine, Type 'off' else type 'on': ")
        if (power == 'off'):
            print("Coffee Machine was shutted off.")
    elif money_input < MENU[menu]["cost"]:
        is_ok = False
        print("Sorry, That is not enough money. The price of coffee is ${0}. Money refunded.\n"\
            .format(MENU[menu]["cost"]))
        power = input("If you turn off the machine, Type 'off' else type 'on': ")
        if (power == 'off'):
            print("Coffee Machine was shutted off.")
        

def report():
    global resources
    if is_ok == True:
        resources["water"] -= MENU[user_want]["ingredients"]["water"]
        resources["milk"] -= MENU[user_want]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_want]["ingredients"]["coffee"]
        resources["profits"] = profits
    return resources



while (power == 'on'):
    if (power == 'off'):
        print("Coffee Machine was shutted off.")
        break
    user_want = input("What would you like? (espresso/latte/cappuccino): ").lower() # selcect menu
    check_resources(menu= user_want) # ingredient check
    if (power == 'off'):
        print("Coffee Machine was shutted off.")
        break
    print("Put your money. You can put\
 quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 only.\n")
    receieve_quarters = int(input("quarters : "))
    receieve_dimes = int(input("dimes : "))
    receieve_nickles = int(input("nickles : "))
    receieve_pennies = int(input("pennies : ")) # receieve money
    check_money(menu= user_want, receieved_quarters= receieve_quarters, receieved_dimes= receieve_dimes,\
        receieved_nickles= receieve_nickles, receieved_pennies= receieve_pennies) # check money

print(resources)