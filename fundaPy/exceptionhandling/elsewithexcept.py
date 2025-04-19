#Else block will execute only when except block was not executed
print("Else with try-except-finally :The code enters the else block only if the try clause does not raise an exception")
#Case 1
print("-"*70)
print("Case 2 : When there is exception is raised inside try block")
try:
    print("Try block")
    print(10/0)
    print("Operation performed")
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally block")
print("-"*70)
print("Case 2 : When there is no exception is raised inside try block")

#Case 2
try:
    print("Try block")
    # print(10/0)
    print("Operation performed")
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally block")
