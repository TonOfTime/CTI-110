
"""
CTI 110
P4T3 - three loops
Taylorg
10/15/2023

Taskes:
- 1: For loop
- 2: While loop
- 3: sentinel loop
"""

# For each of the following
# Ask the user how many cars they saw today
# Find the total and average
day = 1
MAX_DAY = 5
cars_today = 0
cars_total = 0
average = 0
# 1 - for loop
print("Enter how many cars you saw tday?")
for day in range(1, MAX_DAY + 1):
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today

print("Total number of cars seen: ", cars_total)
average = cars_total / MAX_DAY
print("The average of cars seen is: ", average)
print("")

# 2 - While loops
cars_today = 0
day = 1
cars_total = 0
print("")
print("Enter how many cars you saw tday?")
while day <= MAX_DAY:
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
  day += 1
print("Total number of cars seen: ", cars_total)
average = cars_total / MAX_DAY
print("The average of cars seen is: ", average)
print()

# 3 - Sentinel

DONE_VALUE = -1
cars_today = 0
day = 1
cars_total = 0
print("Enter -1 to eit the program.")
keep_going = True
while keep_going:
  print("Cars seen today:", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    keep_going = False

  else:
    cars_total = cars_total + cars_today
    day = day + 1


print("Total cars = ", cars_total)
print("over", day, "days")
average = cars_total / day
print("Average = ", average)