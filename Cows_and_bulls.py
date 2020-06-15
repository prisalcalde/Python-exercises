# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they
# have a “cow”. For every digit the user guessed correctly in the wrong place
# is a “bull.” Every time the user makes a guess, tell them how many “cows”
# and “bulls” they have. Once the user guesses the correct number, the game
# is over. Keep track of the number of guesses the user makes throughout the
# game and tell the user at the end.

# 1. Generate a random number
# 2. Ask the user to guess a 4-digit number
# 3. Compare the numbers (random vs user_guess)
# 4. Create the matching rules for cows and bulls
# 5. If there's a match in the correct place, increment '+1 cow'
# 6. If there's a match in the wrong place, increment '+1 bull'
# 7. If the user guesses the correct number (4 cows, 0 bulls), print 'You win! :)', game is over
# 8. Create a variable for the number of user inputs and increment + 1 on every guess
# 9. Result to end the game: 4 cows, 0 bulls plus the number of times the user had played

import random

random_num = 0
user_guess = 0

def num_compare(random_num, user_guess):
    cow_bull = [0, 0]
    random_num = str(random.randrange(1000, 9999))  # generate random number in a string so it can be treated like a list
    # print("Random:" + str(random_num))
    user_guess = input("Guess a 4-digit number: \n")  # asks the user to guess a number (it'll return a string, so it can be treated like a list)

    for i in range(len(random_num)):
        if random_num[i] == user_guess[i]:  # for each number that is exactly the same, the user gets 1 cow
            cow_bull[0] += 1  # adds a cow to cow_bull list
        elif random_num[i] in user_guess:
            cow_bull[1] += 1  # adds a bull to cow_bull list
        else:
            cow_bull[0] += 0
            cow_bull[1] += 0

    return cow_bull

if __name__ == "__main__": # the code below will only run in this file

    print("""*** Welcome to the Cows and Bulls Game! ***\nYou guess a 4-digit number.\nFor every digit that you guess correctly in the correct place, you'll get a 'cow'.\nFor every digit that you guess correctly in the wrong place, you'll get a 'bull'.\nOnce you guess the correct number, the game is over.\nLet's play!""")

    number_of_plays = 0
    cow_bull_count = [0, 0]

    while cow_bull_count[0] < 5:
        cow_bull_count = num_compare(random_num, user_guess)  # variable to store the cows and bulls = num_compare(random_num, user_guess)
        number_of_plays += 1
        print(str(cow_bull_count[0]) + " cows, " + str(cow_bull_count[1]) + " bulls")

        if cow_bull_count[0] == 4:
            print("Congratulations! You won after " + str(number_of_plays) + " guesses!")
            break
            
