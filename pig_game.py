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
    


