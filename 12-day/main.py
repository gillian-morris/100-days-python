# Dasy 12 - Number Guessing Game
# Thinking about scope, local and global.

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty_guess():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_LEVEL_TURNS
    elif difficulty == "easy":
        return EASY_LEVEL_TURNS

def check_guess(number,actual_answer, attempts_r):
    if number < actual_answer:
        print("Too low.")
    elif number > actual_answer:
        print("Too high.")
    else:
        print(f"You got it! The answer was {actual_answer!s}")
    return attempts_r -1

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess =  random.randint(1,100)

    attempts_remaining = difficulty_guess()
    guess = 0
    while guess != number_to_guess:
        print(f"You have {attempts_remaining!s} remining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts_remaining = check_guess(guess, number_to_guess, attempts_remaining)
        if attempts_remaining == 0:
            print("You've run out of guesses. Rerun the program to try again.")
            return

game()
