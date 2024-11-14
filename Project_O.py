# Blackjack game

import random
import os
import time

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def deal_card():
    """A random card is returned"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take a list of cards and give us their total """
    # Is there blackjack?
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Are the cards above 21 and there is card number 11?
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    results = {
        "draw": "Draw 😊 \n\n",
        "user_over": "You went over 21. Sorry 😔 \n\n",
        "computer_over": "Computer went over 21. You Win! 🌟\n\n",
        "user_21": "You won with a BlackJack 😎🔥",
        "computer_21": "Sorry, computer had a Black Jack 😪 \n\n",
        "user_win": "You win 😍 \n\n",
        "computer_win": "You lose 😢",
    }

    if user_score == computer_score:
        return results["draw"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score >21:
        return results["computer_over"]
    elif user_score == 0:
        return results["user_21"]
    elif computer_score == 0:
        return results["computer_21"]
    elif user_score > computer_score:
        return results["user_win"]
    else:
        return results["computer_win"]

def game():
    print("\nStarting game .....")
    time.sleep(2)
    clear_screen()

    balck_jack = """
    ▀▀█▀▀ ░█──░█ ░█▀▀▀ ░█▄─░█ ▀▀█▀▀ ░█──░█ 　 ░█▀▀▀█ ░█▄─░█ ░█▀▀▀ 
    ─░█── ░█░█░█ ░█▀▀▀ ░█░█░█ ─░█── ░█▄▄▄█ 　 ░█──░█ ░█░█░█ ░█▀▀▀ 
    ─░█── ░█▄▀▄█ ░█▄▄▄ ░█──▀█ ─░█── ──░█── 　 ░█▄▄▄█ ░█──▀█ ░█▄▄▄
    """
    print(balck_jack)

    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n\nYour cards are {user_cards}, current score is {sum(user_cards)}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_continue = False
        else:
            another_card = input("Get another card? (yes/no): ").lower()
            if another_card == "yes":
                user_cards.append(deal_card())
            else:
                game_continue = False

    while computer_score != 0 and computer_score < 17 and user_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n\nYour final hand: {user_cards}, with score {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards} with score {sum(computer_cards)}")
    print(f"\n{compare(user_score, computer_score)}")

while True:
    print("Choose a game to start .....\n")
    print("1- Froggy")
    print("2- Twenty one")
    print("3- Snake")
    print("4- Exit")
    print("---------\n")
    choice = int(input("Enter your choice(1-4): "))
    if choice == 2:
        game()
    else:
        print("Good bye!")
        break