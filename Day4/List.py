"""
Instructions
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
Hints
You might need the help of the len() function. 
https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!

"""
import random
names_string = 'Angela, Ben, Jenny, Michael, Chloe'
# print(names_string)
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

# random_name = random.choice(names)
random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]
# print(random_name)


fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"  # change the last item from Pears to Melons
# print(fruits)
fruits.append("Lemons")
print(fruits)



#Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
# What will be printed?

# What's going on?

# # This question combines several of the Python List concepts that we’ve seen in the previous lessons in isolation. If the code above is at all confusing, I recommend breaking down what’s going on using several print statements using repl.it. First, try printing out:

print(dirty_dozen)
Then print out:

print(dirty_dozen[0])
print(dirty_dozen[1])
# To see what happens at the next stage print out:

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
# I hope this helps clarify how nested lists work. 🙂