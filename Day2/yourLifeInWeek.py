"""
Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 1768 weeks left.

"""
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# 1 year have 52weeks
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")


age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")


def lefeInWeek(age: int) -> str:
    output = ""
    week = 52
    year_left = 90 - int(age)
    week_left = year_left * week
    output = f"You have {week_left} weeks left."
    return output


print(lefeInWeek(53))  # You have 1924 weeks left.
print(lefeInWeek(12))  # You have 4056 weeks left.
print(lefeInWeek(15))  # You have 3900 weeks left.
