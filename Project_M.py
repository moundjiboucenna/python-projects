# Currency converter

import os
import time

exhange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "DZ": 230.0,
    "RMB": 6.5,
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def dispaly_rates():
    print("Welcome to 'Currency converter':\n")
    for currency in exhange_rates:
        print(f"{currency}: {exhange_rates[currency]}")

def currency_converter():
    clear_screen()
    dispaly_rates()

    from_currency = input("\nChoose a currency to convert from: ").upper()
    while True:
        amount = float(input("Enter the amount: "))
        confirmation = input(f"\nYou enterd {amount} {from_currency}. Confirm? (yes/no) ").upper()
        if confirmation == "YES":
            break

    clear_screen()
    dispaly_rates()

    to_currency = input("\nChoose a currency to convert to: ").upper()

    print("Analyzing your request ..... Please wait.")
    time.sleep(2.5)
    print(f"Checking for {to_currency}'s best rates available ..... Please wait.")
    time.sleep(2.5)
    print(f"Getting a discount price for {from_currency} ..... Please wait.")
    time.sleep(2.5)

    if from_currency not in exhange_rates or to_currency not in exhange_rates:
        print("Invalid currency! Conversion canceled.")
        time.sleep(5)
        currency_converter()
    
    new_rate = exhange_rates[to_currency] / exhange_rates[from_currency]
    converted_amount = amount * new_rate

    clear_screen()

    print(f"Preparing the deal from {from_currency} to {to_currency} ..... Please wait.")
    time.sleep(3)
    print(f"Exchange Rate: 1 {from_currency} = {new_rate} {to_currency}")
    time.sleep(3)
    print(f"{amount} {from_currency} is equal to {round(converted_amount, 2)} {to_currency}")
    time.sleep(3)    
     
    accept_transaction = input(f"\nDo you accept this transaction? (Yes/No): ").upper()
    if accept_transaction == "YES":
        print("Tansaction Successful!")
    else:
        print("Transaction Canceled.")

    another_transaction = input("\nDo you want to perform another conversion? (Yes/No): ").upper()
    if another_transaction == "YES":
        currency_converter()
    else:
        print("Thanks for using the currency converter!")
        time.sleep(2.5)

# Start the currency converter
currency_converter()