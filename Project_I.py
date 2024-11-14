# Hangman game

import random

# hangman ascci stages
hangman_stages = ['''
    +---+
        |
        |
        |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''', 
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Choose a random word:
words = ["python", "office", "panda", "apple", "red", "angry", "football", "door"]
random_word = random.choice(words)

# Show spaces with the same number of letters in the word:
display = ["_"] * len(random_word)
print(" ".join(display))

guessed_letters = []
lives = 6
print(hangman_stages[0])

# Ask to guess a letter:
while "_" in display and lives > 0:
    guessed = input("Please guess a letter: ").lower()

    # Has the letter been guessed before?   
    if guessed in guessed_letters:
            print("\nYou already guseed that. try again")
            print(f"You have {lives} more tries\n")
            continue
    
    # Has the letter not been guessed before?
    guessed_letters.append(guessed)

    # If wrong, reduce the lives and display:
    if guessed not in random_word:
        lives -= 1
        print(hangman_stages[6 - lives])

    # If true, replace the space with a letter and display:
    else:
        for position in range(len(random_word)):
            if random_word[position] == guessed:
                display[position] = guessed
                
    print(" ".join(display))
    print(f"\nYou have {lives} more tries\n")

# Show the final result
if lives > 0:
    print("""
        ********
        YOU WIN!
        ********
    """)
else:
    print("""
        *********
        YOU LOSE!
        *********
    """)
    print(hangman_stages[-1])
    print(f"The word was: {random_word}.") 