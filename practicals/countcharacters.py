#Count number of characters in given string

#Take input from user using intput function
givenstr=input("Please enter a string")

#Approach 1 :using len(str) function
nchars=len(givenstr)
print("Appr 1: Number of characters in a given string ::",nchars)

#Approach 2 : using for loop
count=0
for ch in givenstr:
    count+=1

print("Appr 2: Number of characters present in the given str :: ",count)
