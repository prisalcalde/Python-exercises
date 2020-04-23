# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.
# Extras:
# - Keep the game going until the user types “exit”
# - Keep track of how many guesses the user has taken, and when
# the game ends, print this out

# import the random module 
import random

# ask a number between 1 and 9 to the user and store it in num
num = int(input("Guess a number between 1 and 9:\n"))

# generate random number between 1 & 9, including 1 and 9 
# and store it in random_num variable

random_num = random.randrange(1, 10, 1)
print(random_num)

# define too low, too high and exactly right

if num < random_num:
    print("Too low")

if num > random_num:
    print("Too high")

if num == random_num:
    print("Exactly right")
