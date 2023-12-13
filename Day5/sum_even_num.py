"""
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2
52
Example Output 2
702
Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
"""


def sumEvenNum(input):
    sum = 0
    for num in range(2, input + 1, 2):
        sum += num
    return sum


print(sumEvenNum(7))
print(sumEvenNum(100))


def sumEvenNumEven(input):
    sum = 0
    for num in range(1, input + 1):
        if num % 2 == 0:
            sum += num
    return sum


print(sumEvenNumEven(7))
print(sumEvenNumEven(100))
