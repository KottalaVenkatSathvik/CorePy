#Nested exception is nothing try-except block insider another exception block (try-except or try-finally)

#Case 1

try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
        print("Inner operations are performed")
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
    print("Outer operations are performed")
except:
    print("Outer except block")
finally:
    print("Outer finally block")

#Output :
    # Outer try block
    # Inner try block
    # Inner except block
    # Inner finally block
    # Outer finally block

print("-----------------Case 2---------------")

#Case 2

try:
    print("Outer try block")
    print(10/0) #ZeroDivisionError
    try:
        print("Inner try block")
        print(10/0)
        print("Inner operations are performed")
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
    print("Outer operations are performed")
except ValueError: #here we declared ValueError. that means we dont have corresponding except not
    print("Outer except block")
finally:
    print("Outer finally block")

#Output
    # Outer try block
    # Outer except block
    # Outer finally block


print("-----------------Case 3---------------")

#Case 3

try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
        print("Inner operations are performed")
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
    print("Outer operations are performed")
except:
    print("Outer except block")
finally:
    print("Outer finally block")

#Output
# Traceback (most recent call last):
#   File "D:\Python_Projects\CorePy\fundaPy\exceptionhandling\nestedexcept.py", line 34, in <module>
#     print(10/0) #ZeroDivisionError
#           ~~^~
# ZeroDivisionError: division by zero

print("-----------------Case 3---------------")

#Case 3

try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
        print("Inner operations are performed")
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
    print("Outer operations are performed")
except:
    print("Outer except block")
finally:
    print("Outer finally block")

#Output
# Traceback (most recent call last):
#   File "D:\Python_Projects\CorePy\fundaPy\exceptionhandling\nestedexcept.py", line 34, in <module>
#     print(10/0) #ZeroDivisionError
#           ~~^~
# ZeroDivisionError: division by zero 