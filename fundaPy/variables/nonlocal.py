#nonlocal variable used in nested functions
# the nonlocal keyword is used in the case of nested functions.
# This keyword works similarly to the global, but rather than global, this keyword declares a variable to point to the variable of an outside enclosing function, in case of nested functions

def getStudentDetails():
    name="Venkat"
    marks=89
    subject="Maths"
    def subjectStaus():
        nonlocal  marks
        if marks>35:
            return "PASS"
        elif marks==0:
            return "ABSENT"
        else:
            return "Fail"
    status=subjectStaus()
    return name,marks,subject,status

name,marks,subject,status=getStudentDetails()
print(f"Student Details : Name {name}, Subject {subject}, marks :{marks} and Status :{status}")
