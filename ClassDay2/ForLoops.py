my_list = [1,2,3,4]
for i in my_list:
    print(i*2)

s = 'hello how are you'
word_list = s.split()
for word in word_list:
    print(word)

z = 'hello how are you'
word_list = z.split()
for word in word_list:
    if word.startswith('h'):
        print(word)

#modulo --> gives remainder after division
17 % 5
n = 701
if n % 2 == 0:
    print("even number")
else:
    print("odd number")

num_list = [5,700,50,55,61,1017]
for num in num_list:
    if num % 2 == 0:
        print(num, "even number")
    else:
        print(num, "odd number")

# Tuple - similar to a list - cannot be altered
# list
l = [1,2,3]
#tuple (parens)
t = (1,2,3)

employee_salary = [('Victor', 40000), ('Matt', 80000), ('Charles', 100000)]
for employee in employee_salary:
    print(f"Name: {employee[0]} , Salary: {employee[1]}")

employee_salary = [('Victor', 40000), ('Matt', 80000), ('Charles', 100000)]
for (name, salary) in employee_salary:
    print(f"Name:{name}, Salary:{salary}")

d = {'Victor' : 40000,
     'Matt': 80000,
     'Charles': 100000}
for (name, salary) in d.items():
    print(f"Name:{name}, Salary:{salary}")

# TEST: 
# Output:
# start
# s
# sentence
st = 'print only the words that start with s in this sentence'
for word in st.split():
    if word.startswith('s'):
        print(word)

