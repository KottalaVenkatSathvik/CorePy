#  a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.#
# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List are ordered. It maintain the order of elements based on how they are added.
# Accessing items in List can be done directly using their position (index), starting from 0.

list_languages_known=[]

print("_"*25,"add elements using append() ","_"*25)
list_languages_known.append("Java")
list_languages_known.append("Python")
list_languages_known.append("Javascript")
list_languages_known.append("Reactjs")

print(list_languages_known)
for i in list_languages_known:
    print(i,end=",")

print()
print("List of companies =>")
list_of_companies=list(("Google","Meta"))
list_of_companies.append("Apple")
list_of_companies.append("Microsoft")

print(list_of_companies)

print("_"*25,"Repeat list of elements using * ","_"*25)
numbers=[1,8,3]*3
print(numbers)

print("_"*25,"Accessing list elements ","_"*25)
print("First language form the list ",list_languages_known[0])
print("Last language form the list ",list_languages_known[-1])
print("Elements 0 to 2 from the list ",list_languages_known[:3])
print("Elements 2 to last from the list ",list_languages_known[2:])
print("Reverse of the list ",list_languages_known[::-1])

print("_"*25,"Extend list using extend() method","_"*25)
print("Add range(10) to the list numbers :: ",numbers.extend(range(10)))
print(numbers)
print("Add [10,89,45,78,52,47,569,444,14] to another list",numbers.extend([10,89,45,78,52,47,569,444,14]))
print("Add 'Python' to numbers list",numbers.extend('Python'))
print(numbers)

print("_"*25,"Add element at specific index using insert method ","_"*25)
numbers.insert(0,489)
print("Add 489 element at index 0",numbers)

print("_"*25,"Update the element at specific index using insert method ","_"*25)
numbers[-1]=100
print("Update element at last index to 100 ",numbers)

print("_"*25,"Remove element from the list ","_"*25)
numbers.remove(100)
print("Remove element 100 from list  ",numbers)

print("_"*25,"pop method ","_"*25)
numbers.pop()
print("Perform pop operation on numbers ",numbers)
numbers.pop()
print("Perform pop operation on numbers ",numbers)
numbers.pop()
print("Perform pop operation on numbers ",numbers)
numbers.pop()
print("Perform pop operation on numbers ",numbers)
numbers.pop()
print("Perform pop operation on numbers ",numbers)

print("_"*25,"Copy method","_"*25)
copied_numbers=numbers.copy()
print("create a copy of number list :: ",copied_numbers)
copied_numbers[0]=12
print("Update element index 0 to 12 ::",end="")
print(copied_numbers)
print("Original number list :: ",numbers)

print("_"*25,"count number of the time a specific element exist in the list","_"*25)

print("Count of element 2 in the number list",numbers.count(2))
print("Count of element 8 in the number list",numbers.count(8))
print("Count of element 8 in the number list",numbers.count(78))

print("_"*25,"Reverse the list","_"*25)
numbers.reverse()
print(numbers)
print("Reverse copied list :", copied_numbers[::-1])
print("_"*25,"sort the list","_"*25)
numbers.sort()
print(numbers)
print("_"*25,"clear the list","_"*25)
print(numbers.clear())
print(copied_numbers.clear())
print("Copied_numbers ::",copied_numbers)
print("Number list::",numbers)





