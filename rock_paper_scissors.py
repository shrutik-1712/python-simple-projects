import random
def play():
    user = input("rock(r)...ss.paper(p)...scissros(s)\n")
    if user in ['r', 's','p']:
        print("vailded continue\n")
    else:
        print("worng input")
        exit()
    user.lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
print(play())
