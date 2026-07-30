# Day 11 - Blackjack
# Capstone project implementing all beginner python coding concepts reviewed so far

import random
import os
import art

def draw_card(list):
    list.append(random.choice(cards))

def play_game():
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "y":
        os.system("clear")
        print(art.blackjack)
        blackjack()

def check_ace(list):
    if 11 in list and sum(list) > 21:
        post = list.index(11)
        list[post] = 1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    # Draw user cards and computer cards
    user_cards = []
    computer_cards = []
    draw_card(user_cards)
    draw_card(user_cards)
    while sum(computer_cards) < 17:
        draw_card(computer_cards)
        check_ace(computer_cards)
    # Does user want to continue drawing?
    draw = True
    while draw and sum(user_cards)<=21:
        print(f"    Your cards {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            draw_card(user_cards)
            check_ace(user_cards)
        else:
            draw = False
    # Final results
    print(f"  Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"  Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if sum(user_cards) > 21:
        print("You went over. You lose 😭")
    elif sum(user_cards) <=21 and sum(computer_cards) > 21:
        print("Opponent went over. You win 😁")
    elif sum(user_cards) == sum(computer_cards):
        print("Draw")
    elif sum(user_cards) > sum(computer_cards):
        print("You win 😃")
    else:
        print("You lose 😤")
    #Play again?
    play_game()

# Play a game?
play_game()
