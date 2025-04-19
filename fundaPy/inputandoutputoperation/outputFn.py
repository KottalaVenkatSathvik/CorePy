#print() method used as output function in python. It used to print() content in console/screen
#Syntax :
# print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

# value(s): Any value, and as many as you like. Will be converted to a string before printed
# sep='separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
# end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
# file : (Optional) An object with a write method. Default :sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

print("Hi")
#string can be represented with '' or ""

### sep=""#########
# The print() function can accept any number of positional arguments. To separate these positional arguments, the keyword argument “sep” is used.
print(1,2,3,4,5) #defult seperator is whitespace " "  ..OP : 1 2 3 4 5
print(1,2,3,4,5,sep=",") #OP: 1,2,3,4,5
print(1,2,3,4,5,sep="#") #OP: 1#2#3#4#5
print(1,2,3,4,5,sep="@") #OP: 1@2@3@4@5

### end="" #### operator
# The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function.
# By default, “\n”, means new line...
print("Python end operator") #defaullt end="\n", that's why it second print statement prints in newline
print("new line")
#Output
    # Python end operator
    # new line

#end=""
print("Hi Venkat ",end="")
print("Good Morning")
#Output
    #Hi VenkatGood Morning

#file==(Optional) An object with a write method. Default :sys.stdout
print('ADD this content in file', file=open('Testfile.txt', 'w'))


#printing variables
name="Venkat"
address='10011,Street, Gandi Nagar,Hyderbad-000000'
print('Name',name," address :: ",address)
#output
    #Name Venkat  address ::  10011,Street, Gandi Nagar,Hyderbad-000000

#print accepts all escape characters like \n,\t,\r,\\..etc
print("Hi \nVenkat")
#Output
# Hi
# Venkat

print("Hi \tVenkat")
#Output
#Hi 	Venkat

#Append string using + , +operator used to concat/append two strings
#To use + with sting , both should be strings, otherwise it will throw exception
print('Venkat'+'S'+'Kottala') #VenkatSKottala
# print("Venkat"+12) #TypeError: can only concatenate str (not "int") to str

#* repeat operator.. used to repeat any type
print("Venkat "*3)
print((1,5)*3)