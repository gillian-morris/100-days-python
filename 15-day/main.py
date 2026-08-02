# Day 15 - Coffee Machine Program
# Making a "coffee machine" with python

MENU = {
    "latte":{
        "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24
        },
        "cost":2.5
    },
    "espresso": {
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost": 1.5
    },
    "cappuccino":{
        "ingredients":{
        "water":250,
        "milk":100,
        "coffee":24
        },
        "cost":3
    }
}

# Coffee Machine Resources
resources = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

# Report resources
def report(resources):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]:.2f}")

# Check if there is enough water, milk and coffee
def check_resouces(dict_key):
    missing = []
    for key in MENU[dict_key]["ingredients"]:
        if MENU[dict_key]["ingredients"][key] > resources[key]:
            missing.append(key)
    return missing

# Ask user for money
def total_inserted():
    dollar = int(input("How many dollars: "))
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    return (1*dollar) + (.25*quarters) + (.10*dimes) + (.05*nickels) + (.01*pennies)

def make_coffee(dict_key):
    for key in MENU[dict_key]["ingredients"]:
        resources[key] -= MENU[dict_key]["ingredients"][key]
    resources["money"] += MENU[dict_key]["cost"]

# Machine running
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    missing_list = []
    try:
        if order == "off":
            print("Goodbye")
            break
        elif order == "report":
            report(resources)
            continue

        missing_list = check_resouces(order)
        if missing_list:
            print(f"Sorry there is not enough {", ".join(missing_list)}")
        else:
            print(f"Please insert ${MENU[order]["cost"]:.2f}")
            user_inserted = total_inserted()
            if user_inserted >= MENU[order]["cost"]:
                make_coffee(order)
                user_inserted -= MENU[order]["cost"]
                print(f"You get ${user_inserted:.2f} dollars in change.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    except KeyError:
        print("Invalid coffee option. Enter a valid coffee option.")
    except ValueError:
        print("Invalid coin entry. Please enter number of coins.")
