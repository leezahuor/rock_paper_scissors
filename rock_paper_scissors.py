import random

def play_game():
    user = input("Choose one: 'r' for rock, 'p' for paper, or 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return("It's a tie!")
    
    if winner(user, computer):
        return("You won!")
    
    return("You lost!")

#r > s, s > p, p > r
def winner(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True 

print(play_game())