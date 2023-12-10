"""
Create a program that does the following:



Asks the user to enter name of employee
Ask user to enter number of hours the employee worked this week
Ask user to enter employee's pay rate
Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
Calculate amount employee should be paid for regular hours worked.
Display gross pay (total amount that should be paid to employee)
The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
Once finished, submit the finished code file through the assignment link in this folder.




Create a new Python code file named P3HW2_Salary_LastnameFirstname.py
Add a title comment block to the top of the new Python file using the following form:
"""

   # CTI-110

   # P3HW2 - Salary

   # Taylorg3273

   # October 12, 2023

  

employee_name = input("Enter employee's name: ")  
hours_worked = float(input("Enter number of hours worked: "))  
pay_rate = float(input("Enter employee's pay rate: "))  
overtime_hours = 0  
regular_hours = 0  
overtime_pay = 0  
gross_pay = 0  
  
if hours_worked > 40:  
    overtime_hours = hours_worked - 40  
    regular_hours = 40  
else:  
    regular_hours = hours_worked  
  
overtime_pay = overtime_hours * pay_rate * 1.5  
gross_pay = regular_hours * pay_rate + overtime_pay  
  
print("Employee name:", employee_name)  
#print("Pay rate:", pay_rate)  
#print("Number of hours worked:", hours_worked) 
print("---------------------------------------------------------------------------------------")
print("Hours worked\t", "Pay rate\t", "Overtime hours\t", "Overtime pay\t", "Regular Pay\t", "Gross pay")
print("---------------------------------------------------------------------------------------")
print(regular_hours,"\t\t\t\t", pay_rate,"\t\t", overtime_hours,"\t\t\t", overtime_pay,"\t\t", regular_hours * pay_rate,"\t\t\t", gross_pay)
# print("Overtime hours:", overtime_hours)  
# print("Overtime pay:", overtime_pay)  
# print("Gross pay:", gross_pay)