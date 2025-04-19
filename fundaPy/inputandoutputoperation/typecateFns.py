#As we already know that input()function considers every user input as string only
#type casting function can be used to convert one type another type
#Generally python automatically converts the type of the variable once we declare

#Assigining int value to the variable a
a=145
print("Type of the variable a :",a,type(a))
#Reassiagning string value to variable a
a="Venkat"
print("Type of variable a :",a,type(a))

#Expicit Type conversion

#inpt() -> converts the equvalent data type to int type
#Converting string value to int
n1=4.8
n2=int(4.8)
print("Converting ",n1,"to int ::",type(n1)," to int value ",n2,"type ::",type(n2))
# print("Converting ","a","to int ::",type("a")," to int value ",int("a"),"type ::",type(input("a")))
# Traceback (most recent call last):
#   File "D:\Python_Projects\CorePy\inputandoutputoperation\typecastFns.py", line 19, in <module>
#     print("Converting ","a","to int ::",type("a")," to int value ",int("a"),"type ::",type(input("a")))
#                                                                    ^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'a'


#float()-> converts the value into float type
i1=12
f1=float(i1)
print(type(i1),i1)
print(type(f1),f1)

#str() -> converts
i1=14
s1=str(i1)
print(type(i1),i1)
print(type(s1),s1)
