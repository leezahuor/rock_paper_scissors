import random

# Function that plays the actual game. 
def play_game():
    user = input("Choose one: 'r' for rock, 'p' for paper, or 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return(f"The computer chose '{computer}': It's a tie!")
    
    if winner(user, computer):
        return(f"The computer chose '{computer}': You won!")
    
    return(f"The computer chose '{computer}': You lost!")

# r > s, s > p, p > r
# Function that determines if player is winner. 
def winner(player, opponent):
    # Returns True if player wins. 
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True 

print(play_game())