# Puzzle island game

print("""
░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓████████▓▒░ ░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓████████▓▒░    ░▒▓█▓▒░     ░▒▓██████▓▒░   
░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓████████▓▒░ 
                                                                                  
""")

print("Welcome to my island!")
print("there are two doors in front of you.🚪 a red door and🚪 a blue door")
door_choice = input("Which door do you want to open? ").lower()

if door_choice == "red":
  print("Great! now you entered a room.")
  print("You found three boxes: 🎁 white, 🎁 black, 🎁 green")
  box_choice = input("Which box do you open?").lower()

  if box_choice == "white":
    print("Oops! You opened a box filled with snakes! 🐍🐍🐍")
  elif box_choice == "green":
    print("Congratulations! You found the treasure! 💰💰💰")
  elif box_choice == "black":
    print("OOps! You opeed a box filled with spiders! 🕷️🕸️🕷️")
  else:
    print("Invalide choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
elif door_choice == "blue":
  print("Oops! You chose the crocodile door \nGame over! 🐊🐊🐊")
else:
  print("Invalide choice! 🤷‍♂️🤷‍♂️🤷‍♂️")