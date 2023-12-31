from random import randint
from art import logo
'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is 34
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 20
Too low.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 40
Too high.
Guess again.
You have 7 attempts remaining to guess the number.
Make a guess: 30
Too low.
Guess again.
You have 6 attempts remaining to guess the number.
Make a guess: 35
Too high.
Guess again.
You have 5 attempts remaining to guess the number.
Make a guess: 32
Too low.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 34
You got it! The answer was 34.
'''
# Number Guessing Game Objectives:
from art import logo
from random import randint

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_LEVEL = 10
HARD_LEVEL = 5

# Defind the function check answer


def check_answer(guess, answer, turns):
    if guess < answer:
        print('--------------------------------')
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print('--------------------------------')
        print("Too high.")
        return turns - 1
    else:
        print('--------------------------------')
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

# Defind function play_game


def play_game():
    print(logo)
    print('--------------------------------')
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print('--------------------------------')
    answer = randint(1, 100)
    # print(f"The correct answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        print('--------------------------------')
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('----------------')
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print('--------------------------------')
            print("Guess again.")
            print('--------------------------------')


play_game()
