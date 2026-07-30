# Day 09 - Silent Auction
# Using python dictionaries to create a program

import os

bidder_dict = {}
still_bidding = True

while still_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidder_dict[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.")
    os.system('clear')
    if more_bids == "no":
        still_bidding = False

winner = ""
highest_bid = 0
for key in bidder_dict:
    bid_amount = bidder_dict[key]
    if bid_amount > highest_bid:
        winner = key
        highest_bid = bid_amount

print(f"The winner is {winner} with a bid of ${highest_bid!s}")
