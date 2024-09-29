import random

def play():
    user = input("What's your choice? 'r' for rock 'p' for paper and 's' for scissors ")
    computer_choice = random.choice(["r","p","s"])
    if user == computer_choice:
        return "Its a tie!"
    if is_win(user, computer_choice):
        return "You Won!"
    return "You lost!"


def is_win(player,opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
    or (player == "s" and opponent == "p"):
        return True
    

if __name__ == "__main__":
    print(play())
    