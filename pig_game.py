import random #allows you to generate random numbers

def roll(): #function 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of payers (2-4): ")
    if players.isdigit(): #tells us if it is digit or not
        players = int(players) #converts the string (the digit) to an integer
        if 2 <= players <= 4:
            break #if valid then we break out of the while loop
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid. Please enter a number.") #is the input is not a digit

max_score = 50
player_scores = [0 for _ in range(players)] #list of all the scores for all players. Range will loop the number of players we have

while max(player_scores) < max_score:

    for players_ind in range(players):
        print("\nPlayer number", players_ind + 1, "turn has started\n")
        print("Your total score is ", player_scores[players_ind], "\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a ", value)

            print("Your current score is", current_score)

        player_scores[players_ind] += current_score
        print("Your total score is", player_scores[players_ind])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score) #index gives us to index of where the max score is
print("Player number ", winning_idx + 1, "is the winner with a score of ", max_score)

