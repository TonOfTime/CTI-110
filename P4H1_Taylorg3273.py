"""
CTI-110
P4H1
Taylorg3273
"""

num_scores = int(input("Enter the number of scores you would like to enter: "))
#loop asking for scores
scores = []
for score in range(num_scores):
    score_valid = False
    while not score_valid:
        score = int(input("Enter a score: "))
        if score >= 0 and score <= 100:
            score_valid = True
        else:
            print("Invalid score. Please enter a valid score 0-100.")

    scores.append(score)

# Calculate lowest score
lowest_score = min(scores)

# Remove lowest score from list
remove_lowest_score = scores.copy()
remove_lowest_score.remove(lowest_score)

# Calculate average of new list
average_score = sum(remove_lowest_score) / len(remove_lowest_score)

#letter grade if statement
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'


print("--------results--------")
# Print lowest score
print("Lowest score entered:", lowest_score)
print("Modified list\t\t:", remove_lowest_score)

#Averages
print("Average score\t\t:", average_score)
#Your letter grade
print("Letter grade\t\t:", letter_grade)
print("------------------------")