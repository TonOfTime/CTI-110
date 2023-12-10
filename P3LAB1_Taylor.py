#CTI-110
#P3Lab1 - Leap Year
#Taylorg3273
#9/21/23

#calculate if a year is a leap year
#Leap years are:
#Divisible by 4
#unless it's a century, then its divisible by 400

#To do: handle the century case

is_leap_year = False

print("What year to check? ")
year = int(input())

#If the year is divisible by 4, it's a leap year
#We use % , the modulo operator

if year % 4 == 0:
  is_leap_year = True

#Century exception:
#If it's divisible by 100
if year % 100 == 0:
#then it isn't a leap year
  is_leap_year = False
#unless its ALSO divisible by 400 
if year % 400 == 0:
#and then it is a leap year
  is_leap_year = True

#Output the answer
if is_leap_year:
  print(year,"is a leap year.")
else:
  print(year, "is not a leap year.")


