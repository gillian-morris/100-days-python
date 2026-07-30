# Day 07 - Hangman
# Using everything covered so far to create hangman

import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(hangman_words.words))
user_guessed = []

placeholder = []
for let in chosen_word:
    placeholder.append("_")

lives = 6
print(hangman_art.hangman)
while "_" in placeholder and lives > 0:
    print(f"Word to guess: {"".join(placeholder)}")
    guess = input("Guess a letter: ").lower()
    if guess not in user_guessed:
        user_guessed.append(guess)
        if guess in chosen_word:
            for let in range(len(chosen_word)):
                if chosen_word[let] == guess:
                    placeholder[let] = guess
            print("".join(placeholder))
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
    else:
        print(f"You already guessed {guess}")
    print(hangman_art.stages[lives])
    print(f"****************************{lives!s}/6 LIVES LEFT****************************")

if lives > 0 and "_" not in placeholder:
    print(f"************************YOU WIN! IT WAS {"".join(chosen_word)}! ***********************")
else:
    print(f"************************IT WAS {"".join(chosen_word)}! YOU LOSE***********************")
