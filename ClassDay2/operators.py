l = ['x', 'y', 'z']

for i in l:
    if i == 'x':
        print(True)

'x' in ['x', 'y', 'z']
'm' not in ['x', 'y', 'z']

col_names = ['date', 'gender', 'temperature', 'cost_per_day', 'cost_per_night']
[ word for word in col_names if 'cost' in word]

import random
num_list = [1,2,3,4]
random.shuffle(num_list)
print(num_list[2])

random.randint(0,500)

#input - input function always returns a string
fav_color = input("What's your favorite color: ")
if fav_color == "Blue":
    print("So is mine!")
else:
    print("Mine is Blue")


response = input("Enter a number: ")
print(int(response)*2)


from random import randint
def choose_first():
    if randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'