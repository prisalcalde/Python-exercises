# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

def rock_paper_scissors():
    player_1 = input("What's your name? ")
    player_2 = input("And your name? ")
    player_1_answer = input(player_1 + ", rock, paper or scissors? ")
    player_2_answer = input(player_2 + ", rock, paper or scissors? ")
    while True:
        if player_1_answer == "rock" and player_2_answer == "paper":
            print("Congratulations, " + player_2 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                rock_paper_scissors()
                break
            else:
                print("Alright, see you later!")
            break
        if player_1_answer == "rock" and player_2_answer == "scissors":
            print("Congratulations, " + player_1 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1_answer == "paper" and player_2_answer == "scissors":
            print("Congratulations, " + player_2 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1_answer == "paper" and player_2_answer == "rock":
            print("Congratulations, " + player_1 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1_answer == "scissors" and player_2_answer == "rock":
            print("Congratulations, " + player_2 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        if player_1_answer == "scissors" and player_2_answer == "paper":
            print("Congratulations, " + player_1 + "!\nDo you want to start a new game?")
            if input() == "yes":
                print("Great! Let's do it :)")
                break
            else:
                print("Alright, see you later!")
            break
        else:
            player_1_answer = input("It's a tie, let's do it again.\n" + player_1 + ": Rock, paper or scissors? ")
            player_2_answer = input(player_2 + ": Rock, paper or scissors? ")

rock_paper_scissors()
