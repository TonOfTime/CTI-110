#CTI 110
# P5T1 - Functions 
# Garrett Taylor
# 10/24

def main():
  print("Hello world!")
  burger = 4.9900001
  print_money(burger)
  print_money(12)
  print_money(.03)
# main() ends when we stop indenting with tab
# Other functions go here
def print_money(amount):
  print("$", format(amount, ".2f"), sep = "")
#main ends()



# Now, start the program
main()