print("Different Combinations of try-except-else-finally")

print("Case",1,"only try block"," => We get SyntaxError: expected 'except' or 'finally' block")
# try:
#     print("in try block")
#Output:
# File "D:\Python_Projects\CorePy\fundaPy\exceptionhandling\combinationOfTEEF.py", line 5
#     print("in try block")
# SyntaxError: expected 'except' or 'finally' block

print("Case",2,"only except block","=> SyntaxError: invalid syntax")
#
# except ZeroDivisionError:
#     print("except block")

print("Case",3,"only else block","=> SyntaxError: invalid syntax")
#
# else:
#     print("except block")
#Output
    #else:
    #     ^^^^
    # SyntaxError: invalid syntax
print("Case",4,"only finally","=> SyntaxError: invalid syntax")
# finally:
#     print("finally block")
#Output :
    #     finally:
    #     ^^^^^^^
    # SyntaxError: invalid syntax
print("Case",5,"try with except","A valid scenario")
try:
    print("Try Block")
except:
    print("else")

#Output:
#    Try Block

print("Case",6,"try with finally","A valid scenario")
try:
    print("Try Block")
finally:
    print("Finally block")
#Output
    # Try Block
    # Finally block


print("Case",7,"try with else","SyntaxError: expected 'except' or 'finally' block")
# try:
#     print("Try Block")
# else:
#     print("else block")
#Output
    #     else:
    #     ^^^^
    # SyntaxError: expected 'except' or 'finally' block

print("Case",8,"try with else","SyntaxError: expected 'except' or 'finally' block")
# try:
#     print("Try Block")
# else:
#     print("else block")
# finally:
#     print("Finally Block")

#Oputput
    #  else:
    #     ^^^^
    # SyntaxError: expected 'except' or 'finally' block

print("Case",9,"try , except and else","Valid")
try:
    print("Try Block")
except:
    print("except block")
else:
    print("else block")

#Output
    # Try Block
    # else block

print("Case",10,"try with multiple except blocks","Valid")
try:
    print("Try block")
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")

#Output
#Try block

print("Case",11,"try with except and multiple else","InValid : SyntaxError: invalid syntax")
# try:
#     print("Try block")
# except Exception:
#     print("Exception")
# else :
#     print("else1")
# else:
#     print("else")
#Output=>
# else:
#     ^^^^
# SyntaxError: invalid syntax

print("Case",12,"try with one statement between try and except ","InValid : SSyntaxError: expected 'except' or 'finally' block")
# try:
#     print("Try block")
# print("hi")
# except Exception:
#     print("Exception")

#Output
#   print("hi")
#     ^^^^^
# SyntaxError: expected 'except' or 'finally' block

print("Case",13,"independent statement between two except ","InValid : SyntaxError: invalid syntax")
# try:
#     print("Try block")
# except Exception:
#     print("Exception")
# print("test")
# except :
#     print("Exception")

#Output:
# except :
#     ^^^^^^
# SyntaxError: invalid syntax

