

   # CTI-110

   # P4HW2 - Salary

   # Taylorg3273

   # October 12, 2023

regular_hours = 0  
overtime_pay = 0  
gross_pay = 0  
employee_name = input("Enter employee's name or 'Done' to terminate the program: ")

while employee_name != "Done":
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
        overtime_hours = 0.00

    overtime_pay = overtime_hours * pay_rate * 1.5  
    gross_pay = regular_hours * pay_rate + overtime_pay  

  
    print("Employee name:", employee_name)  
    print("---------------------------------------------------------------------------------------")
    print("Hours worked\t", "Pay rate\t", "Overtime hours\t", "Overtime pay\t",   "Regular Pay\t", "Gross pay")
    print("---------------------------------------------------------------------------------------")
    print(hours_worked,"\t\t\t", pay_rate,"\t\t", overtime_hours,"\t\t\t", overtime_pay,"\t\t", regular_hours * pay_rate,"\t\t\t", gross_pay)

    employee_name = input("Enter employee's name or 'Done' to terminate the program: ")