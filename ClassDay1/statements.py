#if - else statements
loc = 'Bank'
if loc == 'Auto Shop':
    print("Welcome to the Auto Shop")
elif loc == 'Bank':
    print('Welcome to the Bank')
else:
    print('where are you?')

#if - else statements
loc = 'Bank'
if loc == 'Auto Shop':
    print("Welcome to the Auto Shop")
elif loc == 'Bank'.lower():
    print('Welcome to the Bank')
else:
    print('where are you?')

#For loops
my_list = [1,2,3,4,5,6,7,8]
#print each number but doubled 
for num in my_list:
    print(num*2)

#print each letter of hello world
s = 'hello world'
for i in s:
    print(i)

#print each letter of hello world
s = 'hello world'
for i in s:
    print(f"this is a letter:{i}")

#list the words in a list
s = 'hello how are you'
word_list = s.split()
for i in word_list:
    print(i)

s = 'hello how are you'
word_list = s.split()
for i in word_list:

    if i[0] == 'h':
        print(i)