# Strong password generator

import random
import string

print("Welcome to the Password Generator!")

lenght = int(input("Enter the total number of characters in the password: "))

num_letters = int(input("Enter the number of letters in the password: "))
num_numbers = int(input("Enter the number of numbers in the password: "))
num_symbols = int(input("Enter the number of symbols in the password: "))

if (num_letters + num_numbers + num_symbols) != lenght:
  print("Invalid input. The sum of letters, numbers and symbols doesn't match the password!")
else:
  letters = random.choices(string.ascii_letters, k = num_letters)
  numbers = random.choices(string.digits, k = num_numbers)
  symbols = random.choices(string.punctuation, k = num_symbols)

  passwrod_chars = letters + numbers + symbols

  random.shuffle(passwrod_chars)

  passwrod = "".join(passwrod_chars)
  
  print("Generated Password:", passwrod)