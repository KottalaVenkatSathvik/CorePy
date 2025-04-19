# Output formatting with various techniques like "".format(),f-string , sep and end operator
# output formatting refers to the way data is presented when printed or logged.
# Proper formatting makes information more understandable and actionable. Python provides several ways to format strings effectively, ranging from old-style formatting to the newer f-string approach.

# Formatting Output using String Modulo Operator(%)
# The string modulo operator (%) is one of the oldest ways to format strings in Python. It allows you to embed values within a string by placing format specifiers in the string. Each specifier starts with a % and ends with a character that represents the type of value being formatted.

print('%2d '%2)
print('%2.3f'%2.8855)
print('Hi %s, welcome to %s programming , your using %f version'%("Venkat","python",3.10))
print("%10.3E" % (356.08977))   # print exponential value
print("%7.3o" % (25))   # print octal value

#Format method
print("Hi {0} , your employee id {1},department {2}".format("Venkat",478855,"IT"))
print("Hi {} , pan number {} , email {} , salary {}".format("Venkat",'ABCD0D011',"test@gmail.com",10.40))
print("Hi {name} , Your salary {sal}".format(name="Venkat",sal="48.665"))


#f-string- used to print variable in convenient way
name="Venkat"
salary=789.25
print(f'Hi {name},salary {salary}')

#sep="" separator used
print(name,salary,sep=",,")
print(name,"welcome to python",sep=",")

#end=""
print("print with default end='\n'")
print("Python lang is easy to learn")
print("python is functional programming lang as well as object oriented program")
print("print with default end=''")
print("Python lang is easy to learn",end="")
print("python is functional programming lang as well as object oriented program")
print("print with default end='@'")
print("Python lang is easy to learn",end="@")
print("python is functional programming lang as well as object oriented program")


import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


cstr = "I love Python and Java lang because both are having best features"

# Printing the center aligned string with fillchr
print("Center aligned: ")
print(cstr.center(40, '#'))

# Printing the left aligned string with "-" padding
print("left aligned: ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("right aligned: ")
print(cstr.rjust(40, '-'))
