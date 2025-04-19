#eval function used to convert the user enter input automatically to corresponding data type
# parse the expression argument and evaluate it as a Python expression and runs Python expression (code) within the program.

input1=input("Please enter a value")
print("Value of the input1 ",input1,", The type of the input1",type(input1))

#By default input() function everything in str only. in order to convert to required data type we need to user type cast functions
# like int(),str()and float()
#eval() function will automatically convert the type based on user input
#       Syntax: eval(expression, globals=None, locals=None)
print("Use eval() function to convert type")
input2=eval(input("Please enter number"))
print("User input ",input2," the type of input2",type(input2))

#Output
    # Please enter a value78
    # Value of the input1  78 , The type of the input1 <class 'str'>
    # Use eval() function to convert type
    # Please enter number789
    # User input  789  the type of input2 <class 'int'>
    #
    # Process finished with exit code 0

