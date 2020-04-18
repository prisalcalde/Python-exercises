
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

# 1. ask the two players input
# 2. when the inputs are different, check if they are "rock", "paper" or "scissors"
# 3. if the inputs are rock and paper, paper wins
# 4. inf the inputs are rock and scissors, rock wins
# 5. if the inputs are scissors and paper, scissors win
# 6. print out a message saying congratulations to the winner
# 7. ask if they want to play a new game
# 8. if the inputs are the same, start again
# 9. end

player_1 = input("Player 1: Rock, paper or scissors? ")
player_2 = input("Player 2: Rock, paper or scissors? ")

def rock_paper_scissors(player_1, player_2):
    while True:
        if player_1 == "rock" and player_2 == "paper":
            print("Congratulations, player 2! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1 == "rock" and player_2 == "scissors":
            print("Congratulations, player 1! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1 == "paper" and player_2 == "scissors":
            print("Congratulations, player 2! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1 == "paper" and player_2 == "rock":
            print("Congratulations, player 1! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1 == "scissors" and player_2 == "rock":
            print("Congratulations, player 2! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1 == "scissors" and player_2 == "paper":
            print("Congratulations, player 1! \nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        else:
            player_1 = input("Play again: Player 1: Rock, paper or scissors? ")
            player_2 = input("Play again: Player 2: Rock, paper or scissors? ")

rock_paper_scissors(player_1, player_2)





