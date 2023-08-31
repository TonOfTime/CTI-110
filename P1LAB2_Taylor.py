"""
CTI-110
P1LAB2 - Sales
8/31
Simple point of sales program.
"""

#set up our store front 
store_name = "ScamStory"
product = "Suprise Boxes"
stock = 50
price = 4.99

#greet customer => explain product => take order => end results
#print () Input () import lines of code of this project
#for punctuation after sentences ,".",sep"" for spacing between last work and punctuation
print("Welcome to", store_name,".",sep="")
print("whats your name?")
customer_name = input()
print("Nice to meet you,", customer_name,".",sep="")

#Explain product
print("Our special today is: ", product, "!",sep="")
print("Only", stock, "left in stock.")

#Take Order
print("How many",product, "would you like?")
#input gives us a string
#order = input()
#convert it to a number
#order = int(order)

#or.....
order = int(input())
# Finish up
#optional
if (order > stock):
  order =stock
  print("Sorry, we can only sell you", order)


total_price = order * price
print("So you would like", order,product,"for a total of $",total_price)
print("<y/n>",sep="")
confrim = input()
if (confrim =="y"):
  print("Shipped!")
else:
  print("Order Canceled.")

print("Thanks for shopping with", store_name, "!")