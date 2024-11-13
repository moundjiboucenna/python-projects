# Rock paper scissors game

import random
# Rock Paper Scissors ASCII Art
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Give information about the game to the user
print("welcome to the Rock, Paper, Scissors game:")
help = input("Press 'Enter' to continue or type (Help) for the rules help: ").capitalize()
if help == "Help":
    print("""
        *********** RULES ***********
        1) You choose and the computer chooses
        2) Rock smashes Scissors -> Rock wins
        3) Scissors smashes Paper -> Scissors wins
        4) Paper smashes Rock -> Paper wins
    """)
# user's choice
user_choice = input("Enter your choice (rock, paper, scissors): ").capitalize()
if user_choice not in ["Rock", "Paper", "Scissors"]:
    print("Invalide choice. Please run the program again and choose rock, paper, or scissors.")
else:
    if user_choice == "Rock":
        print(f"\nYou chose:\n{rock}")
    elif user_choice == "Paper":
        print(f"\nYou chose:\n{paper}")
    else:
        print(f"\nYou chose:\n{scissors}")
            
    #computer's choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if computer_choice == "Rock":
        print(f"\nComputer chose:\n{rock}")
    elif computer_choice == "Paper":
        print(f"\nComputer chose:\n{paper}")
    else:
        print(f"\nComputer chose:\n{scissors}")

    # game result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Scissors" and computer_choice == "Paper") 
        or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")