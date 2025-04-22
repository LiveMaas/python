def greeting():
    print("Hello")

def greeting(name):
    return "Hello " + name
person_name = input("What's your name: ")
response = greeting(person_name)
print(response)

def even_check(number):
    if number % 2 == 0:
        return True
    else:
        return False

if even_check(100):
    print("found an even number")

# Task: Create a function that does the following thing:
# check_even_list()
# Takes a list of integers as input
# if it finds an even number, returns True

number_list = [1,1,4,5,6,7,8]
def check_even_list(number_list):
    for number in number_list:
        if number % 2 == 0:
            return True
    return False
check_even_list(number_list)

# num_list = [2,1,1,5]
# def check_even_list(num_list):
#     for num in num_list:
#         if num % 2 == 0:
#             return True
#     return False

from random import shuffle
def shuffle_list(ply_list):

    shuffle(ply_list)

    return ply_list

shuffle_list([' ','O',' '])

mylist = [' ','O',' ']

def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    
    return mylist

mylist

shuffle_list(mylist)

def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")
    
    return int(guess)

player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)