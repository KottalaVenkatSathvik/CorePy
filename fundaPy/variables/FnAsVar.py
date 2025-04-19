#We can assign function can be assigned to variables, passed as arguments and returned from other functions. Assigning a function to a variable enables function calls using the variable name, enhancing reusability.
shcool_name="ATP Public School"
def student_details(name):
    return  f'Hi {name},Welcome to {shcool_name}'

student=student_details
print(student("Roshan"))
print(student("Rohit"))
print(student("Virat"))
print(student("Rahul"))


def employee_details(name,sal,skills):
    return f'Employee Name :{name},Skills{skills} and salary {sal}'

#here employee will stores the return value
employee_daniel=employee_details("Daniel",44552,['python','javascript',"java"])
#Assigning function to the variable . its is like alias
employee_sam=employee_details

print(employee_daniel)
print(employee_sam("Sam",500000,['python',"java"]))
