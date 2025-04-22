from random import randint
def choose_first():
    if randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
turn = choose_first()
print(turn + "will go first")