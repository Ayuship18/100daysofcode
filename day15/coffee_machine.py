MENU = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.5,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
        },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    }

}

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 100,
}

def is_resource_sufficient(order):
    """returns true when order can be made, otherwise false"""
    for item in MENU[order]:
        if item != 'cost':
            if MENU[order][item] > resources[item]:
                print(f"Sorry there's not enough {item}.")
                return False
            else:
                return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(payment, order):
    if payment >= MENU[order]["cost"]:
        return True
    else:
        print("Sorry not enough coins :()")
        return False


coffee_machine = True

while coffee_machine:
    money = 0
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        coffee_machine = False
        
    elif order == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]} ml.")

    elif order in MENU:
        if is_resource_sufficient(order):
            payment = process_coins()
            if transaction_successful(payment, order):
                change = round(payment - MENU[order]["cost"], 2)
                money += MENU[order]["cost"]
                print(f"Here is the change: ${change}")
                print(f"Here is your {order} ☕️. Enjoy!")
                

            






