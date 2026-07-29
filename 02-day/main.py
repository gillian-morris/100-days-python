# Day 2 - Tip Calculator
# Working with different data types and mathematical operations
print("Welcome to the tip calculator!")
bill = int(input("What is the total bill: "))
tip = int(input("How much tip would you like to give? 10, 12, 15, or other: "))
people = int(input("How many people to split the bill: "))
total = round(bill * ( tip / 100 + 1 ) / people, 2)
print(f"Each person should pay: ${total:.2f}")
