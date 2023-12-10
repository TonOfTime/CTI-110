#CTI-110
#Taylorg3273
#P5Hw1 - Math Quiz
#11/10/23



def main_menu():
     while True:
        print("MAIN MENU")
        print("-----------------------------")
        print("1. Adding random Numbers")
        print("2. Subtracting random numbers")
        print("3. Exit the program")
        selection = input("Please choose one of the meun options: ")
        if selection == "1":
            # This is a function to perform adding random numbers
            def add_random_numbers():
              import random
              num1 = random.randint(1, 100)
              num2 = random.randint(1, 100)
              print(f"What is the sum of {num1} and {num2}?")
              ans = int(input("Enter your answer: "))
              if ans == num1 + num2:
                print("Correct!")
              else: 
                print("Incorrect!")
            add_random_numbers()
              
        elif selection == "2":
            # Call a function to perform subtracting random numbers
            def subtract_random_numbers():
              import random
              num1 = random.randint(1, 100)
              num2 = random.randint(1, 100)
              print(f"What is the result of {num1} - {num2}?")
              ans = int(input("Enter your answer: "))
              if ans == num1 - num2:
                print("Correct!")
              else: 
                print("Incorrect!")
            subtract_random_numbers()
        elif selection == "3":
            print("Thanks for playing try again soon!!")
            break
        else:
            print("Invalid selection. Please try again.")

main_menu()
