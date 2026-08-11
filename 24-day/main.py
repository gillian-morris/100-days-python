# Day 24 - Mail Merger
# Reading and Writing to files in python.

PLACEHOLDER ="[name]"
with open("Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()
with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

for name in name_list:
    s_name = name.strip()
    f_letter = letter.replace(PLACEHOLDER, s_name)
    with open(f"Output/ReadyToSend/{s_name}.txt", "w") as send_file:
        send_file.write(f_letter)
