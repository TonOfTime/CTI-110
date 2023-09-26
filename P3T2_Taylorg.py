"""
CT1 110
P3T2 - Choices and menus
Taylorg3273
9/26/23

"""



#The simplest program, with main()
def main():
  print ("Hello")
  #function call, just use the name with ()
  print("-"*10, "Main Menu", "-"*10)
  print("1.  Lunch")
  print("2.  Dinner")
  print("3.  Dessert")

  #Let the use choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You choose:", choice)
  
#branch (if) on choice
  if choice == 1:
   option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
   print ("Sorry, that's not an option.")
  



  
def option_1():
  print ("Ordering Lunch")
  print("Would you like a burger or a salad.")
  food = input()
  if food == "burger":
    print("One burger, coming up!")
  elif food == "sald":
    print("Your dressing will be on the side.")
    

def option_2():
  print("Ording Dinner")
  print(" Would you like to try our steak or lobster.")
  food = input ()
  if food == "steak":
    print("Steak will be ready in about 20 mins.")
  elif food == "lobster":
    print("This lobster is the best on the east coast.")

def option_3():
  print("Ording Dessert")
  print("Do you want to try out pie or cake")
  food = input ()
  if food == "pie":
    print("You won't regret choosing our world famous pumpkin pie!!")
  elif food == "Cake":
    print("Our sponge cake is the best in the city.")

#Start the program
main()