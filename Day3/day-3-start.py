
"""
Comparison Operators

Operator            Meaning
    >               Greater than
    <               Less than
    >=              Grater than or equal to
    <=              Less than or equal to

"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print(f"YOu can ride the rollercoaster!")

else:
    print(f"Sorry, you have to grow taller before you can ride.")


#  Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print('This is an even number.')
# Otherwise (number connot be divided by 2 with 0 remainder).
else:
    print('This is an odd number.')


# if elif else
