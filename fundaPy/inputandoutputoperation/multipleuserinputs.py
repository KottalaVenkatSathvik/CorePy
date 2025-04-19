# #using input and split() function we can accept multiple inputs from user
# #The split() method splits a string into a list based on a specified separator (by default, it uses whitespace)
# #split() divides the string into separate components based on whitespace by default.
# #we can use any separator
#
name,age,salary=input("Please enter employee name,age and salary").split()
print(name,age,salary)
#
# #Output
# Please enter employee name,age and salary test 45 150000
# test 45 150000
#
name,age,salary=input("Please enter employee name,age and salary").split(" ")
print(name,age,salary)
#
# #Ouptut
# Please enter employee name,age and salary17 89 56
# 17 89 56
#
name,age,salary=input("Please enter employee name,age and salary ").split("$")
print(name,age,salary)
#
# #Output
# Please enter employee name,age and salary 15$12$17
# 15 12 17

#If we want to ask the user for multiple values on a single line,
# we can use list comprehension combined with the input() function and split() to break the input into individual components.
# Also we can take inputs separated by custom delimiter which is comma in the below example.
#Asking multiple user inputs
inputs=[x for x in input("Enter list of numbers").split()]
print(inputs)

#Asking multiple user inputs with split('@@')
inputs=[x for x in input("Enter list of numbers").split("@@")]
print(inputs)

#f you need to collect multiple inputs in a single line and convert them into integers (or another data type),
# the map() function is useful. The map() function applies a specified function to each item in an iterable.

a=map(int,input("Please enter numbers").split(" "))
for i in a:
    print(i)

#Output
# Please enter numbers89 99 663 65
# 89
# 99
# 663
# 65

#Accepting multiple user inputs with for loop

number=int(input("Please enter how many times we need to enter"))
l=list()
for i in (range(number)):
    l.append(int(input("Enter number")))

print(l)

# Please enter how many times we need to enter3
# Enter number1
# Enter number5
# Enter number8
# [1, 5, 8]