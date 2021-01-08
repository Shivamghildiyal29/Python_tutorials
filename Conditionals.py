
#if statement runs the block only when the condition given with the statement is true
if True:
    print("condition was true")

#Checking the variable in the condition
language = "python"
if language=="python":
    print("condition was true")

#when more than 1 condition is given if else is used, else is ececuted only when if condition is not satisfied
#language = "python"
language = "java"

if language=="python":
    print("condition was true")
else:
    print("condition was false")

#using elif condition for more than 2 conditions
language = "python"
#language = "java"

if language == "python":
    print("Language is Python")
elif language == "java":
    print("Language is Java")
else:
    print("No match found")

#boolean operations: and, or and not
# OR -Two or more conditions when the program executes when either one of the conitions is true
language2 == "java"
if language == "python" or language2 == "java":
    print('OR statement is found')

# And -Two or more conditions when the program executes when all conditions are true
a = 'sum'
b='dig'
if A == "sum" and b == "dig":
    print('and statement is found')

# Not -Use to swithced the boolean value
logged_in = "false"
if not logged_in:
    print("Please log in")

# comparision between == and is in python, == compares values whereas is command compares location of objects
a=[12, 51, 36]
b=[12, 51, 36]
c=a
print(a==b) #compares value
print(a is b)#compares the locayion
print(a is c) # is equal to id(a)==id(c)
#finding the id of the object
print(id(a))
print(id(b))
print(id(c))

#False values in pyhton are taken as:
    #False
    #None
    #zero of any numeric type
    #Zero or empty sequence, For example, '', (), []
    #any empty mapping, For example , {}

#Everything other than the abive is taken as true in python

