# A tuple in Python is an immutable ordered collection of elements.
# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered , heterogeneous and immutable

#declare tuple()
print("_"*25,"Creation of tuple ","_"*20)
students=tuple()
colleges=("NITW","IITH","IITB","IITM")
print("Students ",students)
print("Colleges ",colleges)
#create tuple from another list or tuple
list_of_numbers=[18,19,22,14,78,52,69,14]
print("lList of numbers",list_of_numbers)
tuple_of_numbers=tuple(list_of_numbers)
print("Tuple of numbers ",tuple_of_numbers)

print("_"*25,"Access tuple elements ","_"*20)
print("Access colleges at index 0",colleges[0])
print("Access colleges at index 4",colleges[3])
print("Access last college from the colleges ",colleges[-1])
print("_"*25,"Reverse ot tuple using slice operator [::-1 ","_"*20)
print("Reverse pf the tuple ",colleges[::-1])

print("_"*25,"Append two tuple ","_"*20)
tuple1=(1,2,3,4,5)
print("Tuple1 ",tuple1)
tuple2=(5,6,7,8,9)
print("Tuple2 ",tuple2)
tuple3=tuple1+tuple2
print("tuple1+tuple2",tuple3)


