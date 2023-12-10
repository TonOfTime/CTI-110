# CTI 110
# P5LAB1 - CYOA
# Taylorg3273
# 10/26/2023

# first function: main_menu().

from choice import choice_menu


def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        choice_back_door()
        # Call choice 2 here (You can add the corresponding function)
        pass
    elif choice == '3':
        choice_go_home()
        # Call choice 3 here (You can add the corresponding function)
        pass
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("The back door hangs from the hinges you push the door aside and enter with caution...")
    print("You notice 2 stairways one leading to the basment the other leading upstairs")
    
    choice = choice_menu("You start your way up the stairs", "You go down the stairs")
    if choice == "1":
        choice_bedroom()
      
    if choice == "2":
      print("You fall down the stairs GAME OVER")

    

def choice_go_home():
    print("You went home to tell the tale of your adventures.")

# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")


def choice_bedroom():
  print("You make your way up the steps a ghost jumps out and chases you out of the house")
#start the program
main()
