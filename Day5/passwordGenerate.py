# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letters = 4
nr_symbols = 4
nr_numbers = 4


def passwordGenerate(nr_letters, nr_symbols, nr_numbers):
    password = ""
    passwordList = []
    # for char in range(1, nr_letters+1):
    for char in range(nr_letters):
        # or  passwordList += random.choice(letters)
        passwordList.append(random.choice(letters))

    # for char in range(1, nr_symbols+1):
    for char in range(nr_symbols):
        # or  passwordList += random.choice(symbols)
        passwordList.append(random.choice(symbols))

    # for char in range(1, nr_numbers+1):
    for char in range(nr_numbers):
        # or  passwordList += random.choice(numbers)
        passwordList.append(random.choice(numbers))

    random.shuffle(passwordList)
    # Using for loop
    # for char in passwordList:
    #     password += char

    # Using join string
    password = "".join(passwordList)

    return f"Your password is: {password}"


print(passwordGenerate(nr_letters, nr_symbols, nr_numbers))
# return password
