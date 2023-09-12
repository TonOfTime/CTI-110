import matplotlib.pyplot as plt

#collect the data
data = [] #empty list
"""
print("Enter Pokeman data: ")
print("Day 1:", end="")
day1 = int(input())
print("Day 2:", end="")
day2 = int(input())
print("Day 3:", end="")
day3 = int(input())

#put the data in a list
data = [day1, day2, day3]
"""

#New Verison
num_days = 5
for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) #add it to the end of the list

#put the data in a list (DONE)

#TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.ylabel('Pokeman Data')
plt.xlabel ('day #')
plt.ylabel('pokemans collected')
plt.show ()
