# Decryption Project

import string

def decrypt(message, shift):
    alphabet = string.ascii_lowercase

    decrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - shift)
            decrypted_letter = alphabet[new_position]
            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()
            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter

    print(f"\n*** Here is the original message *** \n{decrypted_message}")

user_message = input("Enter a message: ")
shift_number = int(input("Enter a shift number: "))

decrypt(message=user_message,shift=shift_number)