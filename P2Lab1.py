"""
CTI-110
P2LAB1 - Gas Prices
Garrett Taylor
9/7/23

Driving is expensive. Write a program with a car's gas milage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
"""

#Miles per gallon = Miles/Gallons
miles_per_gallon = float(input("What is the car's miles per gallon? "))
#Dollars per gallon $Dollars/Gallons
price_per_gallon = float(input("Price per gallon? "))
#ask for mpg , mpg = float(input("What's the MPG?")) also called the prompt (question)
#Show the price per mile to drive
#unit we want is dollars/miles
price_per_mile = price_per_gallon / miles_per_gallon

#print("This vehicle cost $", price_per_mile, "to drive 1 mile. ")
# f strings are like this {variables: .2f} for 2 decimal places
print(f"This vehicle costs ${price_per_mile:.2f} to drive 1 mile")

#Last step: Tell the user the cost to drive 20, 75 and 500 miles
print(f"This vehicle cost ${price_per_mile * 20:.2f} to drive 20 miles.")
print(f"This vehicle cost ${price_per_mile * 75:.2f} to drive 75 miles")
print(f"This vehicle cost ${price_per_mile * 500:.2f} to drive 500 miles")


