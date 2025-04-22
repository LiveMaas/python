from random import shuffle

def shuffle_list(ply_list):

    shuffle(ply_list)

    return ply_list

def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        
        guess = input("Pick a number: 0, 1, or 2:  ")

    return int(guess)
# def player_guess():

#     response = input("Pick a number: 0, 1, or 2:  ")

#     return int(response)
def check_guess(a_list, ply_guess_int):

    if a_list[ply_guess_int] == 'O':
        print("You won!! Correct guess")
        print(a_list)
    else:
        print("Sorry!! Wrong!!")
        print(a_list)
original_list = [' ','O',' ']

# 1) shuffle that list

mixedup_list = shuffle_list(original_list)

# 2) get the guess

guess = player_guess()

# 3) check the guess

check_guess(mixedup_list, guess)