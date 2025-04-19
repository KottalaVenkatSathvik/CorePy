# A string is a sequence of characters. Python treats anything inside quotes as a string.
# This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.


#Creating string using '' or ""
name="String Data Type"

#Multi line string
aboutme='''
A string is a sequence of characters. Python treats anything inside quotes as a string.
This includes letters, numbers, and symbols. 
Python has no character data type so single character is a string of length 1
'''

print(name)
print(aboutme)

#Accessing string characters inside a string
print(("-"*25),'#Accessing string characters inside a string',("-"*25))

print("First character of the name ",name[0])
print("Last character of the name",name[len(name)-1])
print("Last character of the name with negative index ",name[-1])
# print("Accessing index of out of range lets say 400",name[400])
# IndexError: string index out of range


print(("-"*25),'String slicing operator :: ',("-"*25))
print("Retrieving characters form 1 to 8 ::",name[0:9])
print("Retrieving characters form 1 to 18 ::",name[0:19])
print("Name  ",name[::1])
print("Retrieve every third letter from name::",name[::3])

print("Get All Characters before 8 Position ::",name[:8])
print("Get All Characters after 10 Position ::",name[10:])
print("Retrieve name in reverse order from 8 position to 2",name[-1:-8:-1])
print("Reverse the name ::",name[::-1])

print(("-"*25),'String methods',("-"*25))
print("Length of the name",len(name))
print("Convert name to Upper case ",name.upper())
print("Convert name to lower case ",name.lower())
language=" Python   "
print("remove white space around the ",language," :",language.strip())
print(f"Replace ' ' with ''{language},{language.replace(" ","")} ")
print(f"Check character P present in the string => {'Yes' if 'P' in language else 'NO'}")
print(f"Check character L present in the string => {'Yes' if 'L' in language else 'NO'}")
print(f"Swapcase {language.strip()} => ",language.swapcase())


# capitalize()	Converts the first character of the string to a capital (uppercase) letter
# casefold()	Implements caseless string matching
# center()	Pad the string with the specified character.
# count()	Returns the number of occurrences of a substring in the string.
# encode()	Encodes strings with the specified encoded scheme
# endswith()	Returns “True” if a string ends with the given suffix
# expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
# find()	Returns the lowest index of the substring if it is found
# format()	Formats the string for printing it to console
# format_map()	Formats specified values in a string using a dictionary
# index()	Returns the position of the first occurrence of a substring in a string
# isalnum()	Checks whether all the characters in a given string is alphanumeric or not
# isalpha()	Returns “True” if all characters in the string are alphabets
# isdecimal()	Returns true if all characters in a string are decimal
# isdigit()	Returns “True” if all characters in the string are digits
# isidentifier()	Check whether a string is a valid identifier or not
# islower()	Checks if all characters in the string are lowercase
# isnumeric()	Returns “True” if all characters in the string are numeric characters
# isprintable()	Returns “True” if all characters in the string are printable or the string is empty
# isspace()	Returns “True” if all characters in the string are whitespace characters
# istitle()	Returns “True” if the string is a title cased string
# isupper()	Checks if all characters in the string are uppercase
# join()	Returns a concatenated String
# ljust()	Left aligns the string according to the width specified
# lower()	Converts all uppercase characters in a string into lowercase
# lstrip()	Returns the string with leading characters removed
# maketrans()	 Returns a translation table
# partition()	Splits the string at the first occurrence of the separator
# replace()	Replaces all occurrences of a substring with another substring
# rfind()	Returns the highest index of the substring
# rindex()	Returns the highest index of the substring inside the string
# rjust()	Right aligns the string according to the width specified
# rpartition()	Split the given string into three parts
# rsplit()	Split the string from the right by the specified separator
# rstrip()	Removes trailing characters
# splitlines()	Split the lines at line boundaries
# startswith()	Returns “True” if a string starts with the given prefix
# strip()	Returns the string with both leading and trailing characters
# swapcase()	Converts all uppercase characters to lowercase and vice versa
# title()	Convert string to title case
# translate()	Modify string according to given translation mappings
# upper()	Converts all lowercase characters in a string into uppercase
# zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string