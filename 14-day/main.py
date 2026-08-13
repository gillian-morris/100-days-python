# Day 14 - Higher or Lower Game
# Using all python from the class so far in one game

import os
import random
from game_data import data
import art

def check_guess(user_guess, option_a, option_b):
    if user_guess == "A":
        if option_a["follower_count"] >= option_b["follower_count"]:
            return True
        else:
            return False
    elif user_guess == "B":
        if option_a["follower_count"] <= option_b["follower_count"]:
            return True
        else:
            return False
    else:
        return False

def print_vs(option_a, option_b):
    print(f"Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}")
    print(art.vs)
    print(f"Compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}")

def play_game(option_a, option_b, score):
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if check_guess(guess, option_a, option_b):
        score += 1
        option_a = option_b
        option_b = random.choice(data)
        os.system("clear")
        print(art.logo)
        print(f"You're right! Current score: {score!s}.")
        print_vs(option_a, option_b)
        play_game(option_a, option_b, score)
    else:
        os.system("clear")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score!s}")

option_a = random.choice(data)
option_b = random.choice(data)
score = 0

os.system("clear")
print(art.logo)
print_vs(option_a, option_b)
play_game(option_a, option_b, score)
