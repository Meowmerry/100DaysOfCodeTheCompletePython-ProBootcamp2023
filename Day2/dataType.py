# Data Type

# String
string = "Hello"
print(string[0])  # Prints the first character ('H')
print(string[len(string) - 1])  # Prints the last character ('o')


# Interger
nums = 124 + 456
print(nums)


# Float
my_float = 3.14159
mystery = 734_529.678
print(my_float)
print(mystery)


# Boolean
True
False


# Checking Data Types
num_char = len(input("What is your name?"))
my_name = len("Meow")
print(type(my_name))  # <class 'int'>
string_name = str(my_name)
print(type(string_name))  # <class 'str'>


print(type(70 + float("100.5")))  # 170.5  <class 'float'>


'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

The last line of your program should print the result.

Example 1 Input
39

Example 1 Output
12
Example 2 Input
43

Example 2 Output
7
'''
two_digit_number = input()  # input will give us the String type
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)


########################################################################
# Arithmetic Operators, you can do mathematical calculations with Python as long as ou know the right operators
# Add
3+2

# Subtract
4 - 1

# Multiply
2 * 3

# Divide
5 / 2  # when you use divide will always be flot type

# Exponent
5 ** 2

# PEMDAS
# ()
# **
# *  /
# +  -

print(3 * 3 + 3 / 3 - 3)  # 7.0
print(3 * (3 + 3) / 3 - 3)  # 3.0

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# height * height    return weight_kg / (height_m ** 2)
# Write your code below this line 👇
weight_as_int = int(weight)
height_as_int = float(height)
# or  (height_as_int ** height_as_int)
my_BMI = weight_as_int / (height_as_int ** 2)
print(int(my_BMI))


#########  round function  ############
print(round(8/3, 2))  # 2.67
print(round(2.755555555, 2))  # 2.76
print(8 // 3)  # 2


result = 4 / 2
result /= 2
print(result)  # 1.0
print(round(result))  # 1

# f funciton string ---> f" "
score = 0
height = 1.8
isWinning = True
print(
    f"your score is {score}, your height {height}, your are wining is {isWinning}")  # your score is 0, your height 1.8, your are wining is True
