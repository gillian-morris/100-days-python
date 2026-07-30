# Day 10 - Calculator
# More functions but this time with returns
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operator_dict = {"+":add, "-":sub, "*":mult, "/":div}

def calculator():
    continue_calc = True
    user_n1 = float(input("What's the first number?: "))
    while continue_calc:
        for key in operator_dict:
            print(key)
        user_operator = input("Pick an operaion: ")
        user_n2 = float(input("What's the next number?: "))
        user_n1 = operator_dict[user_operator](user_n1, user_n2)
        new_calculation = input(f"Type 'y' to continue calculating with {user_n1}, or type 'n' to start a new calculation: ")
        if new_calculation == 'n':
            continue_calc = False
            calculator()
calculator()
