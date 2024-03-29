MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 2.5
}


def enoughIngredients(drink):
    if drink != "report":
        order = MENU[drink]["ingredients"]
    if drink == "espresso":
        if resources["water"] < order["water"]:
            print("Sorry there is not enough water")
        elif resources["coffee"] < order["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            payment(drink)

    elif drink == "latte":
        if resources["water"] < order["water"]:
            print("Sorry there is not enough water")
        elif resources["milk"] < order["milk"]:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < order["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            payment(drink)

    elif drink == "espresso":
        if resources["water"] < order["water"]:
            print("Sorry there is not enough water")
        elif resources["milk"] < order["milk"]:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < order["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            payment(drink)

    else:
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${resources["money"]}")


def payment(drink):
    print("Please insert your coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[drink]["cost"]

    if total < cost:
        print("Sorry that's nout enough money. Money refunded.")
    else:
        change = total - cost
        resources["money"] += cost
        print(f"Here is your change: ${round(change,3)}")
        reportUpdate(drink)

def reportUpdate(drink):
    order = MENU[drink]["ingredients"]
    resources["water"] = resources["water"] - order["water"]
    resources["milk"] = resources["milk"] - order["milk"]
    resources["coffee"] = resources["coffee"] - order["coffee"]
    print(f"Here is your {drink}. Enjoy!")


while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        print("Goodbye")
        break
    else:
        enoughIngredients(request)







