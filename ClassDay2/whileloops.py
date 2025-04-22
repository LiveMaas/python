#while loops
x = 0

while x < 5:
    print('x is currently: ',x)
    print(' x is still less than 5, adding 1 to x')
    x+=1

x = 0

while x < 5:
    print('x is currently: ',x)
    print(' x is still less than 5, adding 1 to x')
    x+=1
    
else:
    print('Complete')

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

response = True

while response:
    # game 

    # print("do you want to keep playing?)
    # answer <-- user
    # if answer == "yes":
    # response = False