# CTI-110
#P5Lab2 - Functions
#Taylorg3273
#11-2-23

#First print a table of squares

def main():
  print("P5LAB2")
  print("number\tnumber squared")
  # range(1,11) gives numbers 1-10
  for num in range(1, 11):
    num_squared = square(num)
    print_row(num, num_squared)



def square(number):
  """input: a number
  output: the number squared."""
  square = number * number
  return square

# print_row() is a void function
def print_row(num, num_squared):
    print(num, "\t\t", num_squared)

# START PROGRAM
main()
