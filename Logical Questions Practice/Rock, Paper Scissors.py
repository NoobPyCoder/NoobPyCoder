import random
# r > s, s > p, p > r

def play():
    user = input("What is your choice : 'r' for rock, 'p' for paper, 's' for scisoors - ")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a tie"

    if is_win(user, computer):
        return "You won."
    
    return "You lost."

def is_win(player, opponent):
    # return true if palyer wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
