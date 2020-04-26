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

if num == random_num:
    print("Exactly right")
    
elif num > random_num:
    print("Too high")
    
else:
    print("Too low")


# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when
# the game ends, print this out
import random

def guessing_game(count = 0): # defines function and count variable starting with 0
    num = int(input("Guess a number between 1 and 9:\n"))
    random_num = random.randrange(1, 10, 1)
    print(random_num)
    count += 1  # adds 1 each time the the function is called

    while True:

        if num == random_num:
            print("Exactly right, type 'exit' to end the game or press any key to continue")

        elif num > random_num:
            print("Too high, type 'exit' to end the game or press any key to continue")

        else:
            print("Too low, type 'exit' to end the game or press any key to continue")

        if input() == "exit":
            print('count: %d' % count)
            exit(0)

        guessing_game(count) # calls the function with the incremental count

guessing_game()

