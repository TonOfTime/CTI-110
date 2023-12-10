# CTI 110
# P4Lab1 - Part B
# Text "graphics"
# Taylorg
# 10/5/2023

#Draw a rectangle with text
char = "🦷"
#print (Char)

#Part 1: Draw a horizontal line
#width = 10
#height = 10

width = int(input("How wide is the rectangle? "))
height = int(input("How tall is it? "))


print("Printing", width, "columns")
for column in range(width):
    #don't go to a new line
    print(char, end="")
print()

# Part 2 : Vertical line
for row in range (height):
    print(char) # we want the new line

for row in range(height):
    for column in range(width):
        print(char, end="")
    print() #end the line
