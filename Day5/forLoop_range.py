# for loops and the range() function
for num in range(1, 10):  # will print only 1 - 9, not includes 10
    print(num)  # 1,2,3,4,5,6,7,8,9


for num in range(1, 10, 3):  # will print every step by 3
    print(num)  # 1,4,7


target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for number in range(0, 1001):
    total += number
print(total)
