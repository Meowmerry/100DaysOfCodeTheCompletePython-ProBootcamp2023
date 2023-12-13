"""
Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
"""

# Input a list of student scores


def findStudentHeightScore(input):
    student_scores = input.split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

    # Write your code below this row 👇
    hight_score = 0
    for score in student_scores:
        if hight_score < score:
            hight_score = score
    return f"The highest score in the class is: {hight_score}"


input = '78 65 89 86 55 91 64 89'
print(findStudentHeightScore(input))
input1 = '150 142 185 120 171 184 149 199'
print(findStudentHeightScore(input1))
input2 = '24 59 68'
print(findStudentHeightScore(input2))


### SOLUTION ##

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)

print(f"The highest score in the class is: {highest_score}")
