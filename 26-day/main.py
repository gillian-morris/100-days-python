# Day 26 - NATO Alphabet Project
# Reviewing List Comprehension and more pandas
#
import pandas

# Create a dictionary
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
code_list = [nato_dict[let] for let in user_input if let != " "]
print(code_list)
