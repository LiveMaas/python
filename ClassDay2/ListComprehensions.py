# list comprehensions -- for loop in 1 one line
#add even numbers to even num list and odd to odd num list
number_list = [1,2,3,4,5,6,7,8,9,10]
even_num_list = []
odd_num_list = []
for num in number_list:
    if num % 2 ==0:
        even_num_list.append(num)
    else:
        odd_num_list.append(num)

#evens in one line
[num for num in number_list if num % 2 ==0]

#Other Comprehension statements
["even" if num % 2 ==0 else "odd" for num in number_list]
print(["even" for num in number_list if num % 2 ==0 ])
print(["odd" for num in number_list if num % 2 !=0 ])

# TEST:
# you can use .append()
# len()
# Bonus: as list comprehension
# Output:
# ['Add', 'every', 'has', 'odd', 'letters', 'a']
len()
st = 'Add every word in this sentence that has an odd number of letters to a list'
words = st.split()
odd_words = []
for word in words:
    if len(word) % 2 != 0:
        odd_words.append(word) # <--- had "words" in here creates crazy output
        print(odd_words)

odd_list = [word for word in st.split() if len(word) % 2 == 1]
print(odd_list)