#string is hello world, print is function
#print("Hello World")

#type(), print(), len()
s = "Hello World"
#prints output in quotes
print(s)
#counts the numbers in hello world
len(s)
#shows type of variable
type(s)
#outputs indexed number, starts at 0
s[6]
#reverse index -1 gives output in reverse -1 gives d
s[-1]
#slicing gets piece of the text below outputs Hello, leaving one side empty gives you everything after or before that number
s[0:5]
#step sizing outputs Hlo
s[0:5:2]
#s[::-1] --> 'dlroW olleH'
#string properties, below does not support item assignment (immuntability)
s[0] = 'x'
#concatenation --> + 
#x + "hello world"
#"x" + "hello world"
#'xhello world'
#"x" + "hello world"[1:]
#'xello world'
#x + s[-1]

#String methods https://www.w3schools.com/python/python_ref_string.asp
s.capitalize()
s.upper()
#s = s.upper() <-- makes all upper case
s.find()
s.split()

txt = "welcome! to! the! jungle!"

x = txt.split("!") #default is space

print(x)
 
# .format()
name = "Steve"
age = 42
salary = 1

#print("Name: " +  name +  "Age: "+ str(age) +  "Salary: " + str(salary) )

print("Name: {} Age: {} Salary: {}".format(name, age, salary))

#f-string

print(f"Name: {name}, Age: {age} Salary {salary}")
