#Global variables are accessible anywhere in the file
#it generally common for all functions in side file

school_name="ZPHS"

#define student_details,

def student_details():
    '''
    To print student details like name,school name and total_marks secured

    '''
    # global school_name
    name="Venkat"
    total_marks=550
    print("Hi {} , school ::{}  and your total secured marks are {}".format(name,school_name,total_marks))

student_details()

#Output :
#   Hi Venkat , school ::ZPHS  and your total secured marks are 550

print("Print School name outside fn",school_name)
#Accessing and update global variables inside function

def update_school_name():
    global school_name
    school_name="Narayana shcool"
    print("Updating school name ")
    print("School name in update_school_name",school_name)

update_school_name()
print("Print School name outside fn",school_name)