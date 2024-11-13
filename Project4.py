# Books manger

# Step 1: Setup
library = []
wishlist = []

# Step 2: Adding books
book_name = input("Enter the name of a book you own: ")
library.append(book_name)

book_name = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book_name:
  library.append(book_name)

print("\nYour Library:", library)

# Step 3: Managing the Wishlist
book_name = input("\nEnter the name of a book you wish th have in the future: ")
wishlist.append(book_name)

book_name = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if book_name:
  wishlist.append(book_name)

print("\nYour Wishlist:", wishlist)

# Step 4: Mergin Wishlist into Library
acquired_book = input("\nEnter the name of a book from your wishlist  that you've acquired (or press 'Enter' to skip): ")
if acquired_book in wishlist:
  library.append(acquired_book)
  wishlist.remove(acquired_book)

print("\nUpdate Library:", library)
print("Update Wishlist:", wishlist)

# Step 5: Donated book
donated_book = input("\nEnter the name of a book from your library you wish donate (or press 'Enter' to skip): ")
if donated_book in library:
  library.remove(donated_book)

print("\nFinal library after donations: ", library)