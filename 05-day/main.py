# Day 5 - Password Generator
# Using python for loops to generate a random string

import random

lower = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_special = int(input("How many symbols ould you like?\n"))

password = []

for num in range(nr_letters):
    password.append(random.choice(lower))

for num in range(nr_numbers):
    password.append(random.choice(numbers))

for num in range(nr_special):
    password.append(random.choice(special))

random.shuffle(password)
print("Your password is: " + "".join(password))
