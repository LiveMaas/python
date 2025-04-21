name = "Jim"
age = 42
salary = 1

#lists
l = [1,2,3]
m = ['taco', 23, 1, True]
len(m)
m[1:3]
m[0] = 'burrito'
m.append('84')
m.append('84')
print(m.count('84'))
m.pop(1)
print(m)

removed_item = m.pop(3)
n = [1,5,8,9,5,4,3]

#Nesting Lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
m2 = [lst_1, lst_2, lst_3]
print(m2)
m2[-1][-1]
