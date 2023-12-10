"""
CT1-110
Taylorg3273
P3HW1
10/1/2023
"""
"""
P3HW1 - Letter Grades

For P3HW1, you will complete the exercise below.

In this assignment you are building on P2HW2_Lists. Only for this assignment, you are given a partial program with bugs. You are to correct the program and complete it.

NOTE: Sometimes when you get a buggy, incomplete program, it may be easier to just start over. I'm not definitely saying that's true this time -- but you should keep it as an option.



REQUIREMENTS

The program is supposed to do two things:

Find the average score for a student (a number from 0 to 100)
Find the letter grade (a string, "A", "B", etc.) based on that number, using the ten point scale.

"""
#add the grades in a list

Module_1 = float(input("Enter your grade for module 1: "))
Module_2 = float(input("Enter your grade for module 2: "))
Module_3 = float(input("Enter your grade for module 3: "))
Module_4 = float(input("Enter your grade for module 4: "))
Module_5 = float(input("Enter your grade for module 5: "))
Module_6 = float(input("Enter your grade for module 6: "))

my_list = [Module_1,  Module_2, Module_3, Module_4, Module_5, Module_6]

#Determine the lowest, highest, sum and average for the grades

low = min(my_list)
high = max(my_list)
sum = sum(my_list)
avg = sum / len(my_list)



print ("-------Results-------")


letter_grade = "G"

if avg >= 90:
  letter_grade = "A"
elif avg >= 80:
  letter_grade = "B"
elif avg >= 70:
  letter_grade = "C"
elif avg >= 60:
  letter_grade = "D"
elif avg <= 59:
  letter_grade = "F"
#print the letter grade
print("A grade of", f"{(avg):.02f}" , "is a", letter_grade)