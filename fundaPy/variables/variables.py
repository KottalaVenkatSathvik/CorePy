# variables are used to store data that can be referenced and manipulated during program execution.
# Variables act as placeholders for data. They allow us to store and reuse values in our program

#Example
print("--------------------------------------Declare variable-------------------------------")
lang="Python"
age=22
sal="89998.55444"
#--------------------------------------Rules to declare variables---------------------
print("--------------------------------------Rules to declare variables---------------------")
#1. Variable should have numbers, letters and _,
name="VenkatK"
print(name)
#Output
    #"VenkatK"

_age=25
print(_age)
#OUTPUT
    # 25

name2="Kottala"
print(name2)
#-----------------------2.variable should not be start with digits--------------------------------
print("-----------------------2.variable should not be start with digits--------------------------------")
#1a=41
#print(1x)

#Output
    # File "variables.py", line 18
    #     1a=41
    #     ^
    # SyntaxError: invalid decimal literal

#--------------------------------2.We should not use reserved keyword----------------------------------
# if=41

# File "variables.py", line 33
#     if=41
#       ^
# SyntaxError: invalid syntax

#-----------------------3. variables are case sensitive--------------------------------------------
a=145
A=146
print(a,A)

#---------------------------Dynamic programing-----------------------------------------------------
print("---------------------------Dynamic programing-----------------------------------------------------")
x = 8
x="Venkat"
print(x)

#Output
# Venkat
#------------------------------------#Assigning multiple variable------------------------------------------------
print("------------------------------------#Assigning multiple variable------------------------------------------------")
#Assigning multiple variable
n1,n2,n3 =12,25,36

print(n1,n2,n3,sep=",")

#Output
# 12,25,36

#---------------------------------------#Object reference-----------------------------------------------
print("---------------------------------------Object reference-----------------------------------------------")
#Object reference
#let create  a variable a,b different values

a="Venkat"
b="Swamy"

print("Address of a :", a, id(a),"Address of b :",b,id(b))
print("Address of a and b are same "if id(a)==id(b) else "Address of a,b are different")

print("Assign a, b variable with same value")

a="Iris"
b="Iris"

print("Address of a :",a, id(a),"Address of b :",b,id(b))
print("Address of a and b are same "if id(a)==id(b) else "Address of a,b are different")

#-------------------------------Type of the variables-------------------------------------------------------
print("-------------------------------Type of the variables-------------------------------------------------------")
emmpno=123
empname="Venkat"
edepart="IT"
esal=789788.55
ismarried=False
languages_known=["Python","Java","Javascript"]

print('Type of emmpno value, type', emmpno, type(emmpno))
print("Type of empname value, type",empname,type(empname))
print("Type of edepart value, type",edepart,type(edepart))
print("Type of esal val,type",esal,type(esal))
print("Type of ismarried val,type",ismarried,type(ismarried))
print("Type of languages_known val,type",languages_known,type(languages_known))
#--------------------------------------------------del variables--------------------------------------------
print("delete empname , edepart")
del empname
del edepart
# print("Access empname , edepart",empname,edepart)

# Traceback (most recent call last):
#   File "variables\variables.py", line 105, in <module>
#     print("Access empname , edepart",empname,edepart)
#                                      ^^^^^^^
# NameError: name 'empname' is not defined
