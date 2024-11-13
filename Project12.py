# Library management

import os

library = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_book():
    while True:
        clear_screen()
        isbn = input("Enter ISBN: ")
        while True:
            if isbn.isdigit():
                break
            else:
                print("That's not ISBN!")
                isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")

        library[isbn] = {"title": title, "author": author, "available": True}

        print(f"Book '{title}' by '{author}' added to the catalog with ISBN {isbn}.")

        choice = input ("Do you want to add another book? (yes/no): ")
        if choice.lower() != "yes":
            break
    
def check_out_book():
    while True:
        clear_screen()
        isbn = input("Enter ISBN to chek out: ")
        while True:
            if isbn.isdigit():
                break
            else:
                print("That's not ISBN!")
                isbn = input("Enter ISBN to chek out: ")
            
        if isbn in library:
            if library[isbn]["available"]:
                library[isbn]["available"] = False
                print(f"Book '{library[isbn]["title"]}' checked out successfully.")
            else:
                print("Sorry, the book is currently checked out.")
        else:
            print("Book not found in the library.")
        
        choice = input ("Do you want to chek out another book? (yes/no): ")
        if choice.lower() != "yes":
            break

def check_in_book():
    while True:
        clear_screen()
        isbn = input("Enter ISBN to check in: ")
        while True:
            if isbn.isdigit():
                break
            else:
                print("That's not ISBN!")
                isbn = input("Enter ISBN to chek in: ")

        if isbn in library:
            if not library[isbn]["available"]:
                library[isbn]["available"] = True
                print(f"Book '{library[isbn]["title"]}' checked in successfully.")
            else:
                print("The book is already available in the library.")
        else:
            print("Book not found in the library.")
        
        choice = input ("Do you want to chek in another book? (yes/no): ")
        if choice.lower() != "yes":
            break

def list_books():
    clear_screen()
    print("Library Books:")
    for isbn in library:
        book_info = library[isbn]
        print(f"ISBN: {isbn}, Title: {book_info["title"]}, Author: {book_info["author"]}, Available: {book_info["available"]}")
    input("Press enter to return to the main program...")

while True:  
    print("\nMenu:")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    
    elif choice == "2":
        check_out_book()

    elif choice == "3":
        check_in_book()

    elif choice == "4":
        list_books()

    elif choice == "5":
        print("\nExiting the program...")
        break

    else:
        clear_screen()
        print("Invalid choice! Please enter a number between 1 and 5.")