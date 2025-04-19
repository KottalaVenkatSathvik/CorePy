#Local variables are accessed only inside the the function


#define function
def greetFn():
    '''
    To print greeting message
    :return:
    '''
    name="Venkat"
    print(f"{name},Good Morning")
    return None
greetFn()
#Local variables are not accessible outside the function, if we try to access local variable 'name' , we get error NameError
#print(name) #NameError: name 'name' is not defined

#define student_details function
def student_details():
    '''
    To print student_details like name, school_name and class_name
    :return:
    '''
    name="Venkat"
    school_name="ZPH SCHOOL"
    class_name=9
    print(f'Hi {name}, school :{school_name} and your class is {class_name}')

student_details()
