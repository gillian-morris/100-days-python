# Day 08 - Ceasar Cipher
# Using functions with parameters

def ceasar(encode_or_decode,origin_text,shift_amount):
    word = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in origin_text:
        if letter in alphabet:
            post = (alphabet.index(letter) + shift_amount) % len(alphabet)
            word += alphabet[post]
        else:
            word += letter
    print(f"Here is the {encode_or_decode}d result {word}")

again = True
while again:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))

    if direction == "encode" or direction == "decode":
        ceasar(direction,text,shift)
    else:
        print("Invalid option please type 'encode' or 'decode'.")
        continue

    user_again = input("Would you like to encode or decode something else? 'yes' or 'no'\n").lower()
    if user_again == 'no':
        again = False
