# Day 04 - Rock, Paper, Scissors
# Randomization in Python
import random

list = ["rock", "paper", "scissors"]

computer = random.choice(list)
user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))
user = list[user_choice]
print("Computer Chose " + computer)
print("You Chose " + user)
if user == computer:
    print("Tie, try again.")
elif (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors") or (user == "scissors" and computer == "rock"):
    print("You Lose")
elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
    print("You Win")
else:
    print("Invalid input")
