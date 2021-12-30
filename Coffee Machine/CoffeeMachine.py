from Data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_off_machine = False
money = 0
change = 0
missing_item = ""

def coins(selection):

    global change
    global money

    change = 0
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many dimes?: "))
    pennies = float(input("How many pennies?: "))

    total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    beverage_price = MENU[selection]['cost']

    if total_coins > beverage_price:
        money += beverage_price
        change = round(total_coins - beverage_price,2)
        return True
    elif total_coins < beverage_price:
        return False

def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"

def make_coffe(beverage):
    global missing_item
    missing_item = ""
    water =  resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    for element in MENU[beverage]['ingredients']:
        if MENU[beverage]['ingredients'][element] > resources[element]:
            missing_item = element
            return False
        elif MENU[beverage]['ingredients'][element] <= resources[element]:
            resources[element] = resources[element] - MENU[beverage]['ingredients'][element]

    return True

while not turn_off_machine:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        print("Machine Turned Off")
        turn_off_machine = True
    elif selection == "report":
        print(report())
    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        beverage = make_coffe(selection)
        if beverage:
            price = coins(selection)
            if price:
                print(f"Here is ${change} in change.")
                print(f"Here is your {selection} ☕️. Enjoy!")
            elif not price:
                print("Sorry that's not enough money. Money refunded.")
        elif not beverage:
            print(f"Sorry there is not enough {missing_item}")

