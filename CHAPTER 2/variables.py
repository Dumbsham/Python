import sys

# print(sys.version)
#to check python version

'''in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.'''
# variables do not need to be declared with any particular type,and can even change type after they have been set

x = 4

x = "sali"

print(x)

#casting: in order to specify the data type of a variable,this can be done with casting

x = str(3)
y = int(3)
z = float(3)
a = "saksham" # can also be 'saksham' because string variables can be declared either by using single or double quotes
print(x," ",y," ",z)

#we can get the data type of a variable with type() function

print(type(x))
print(type(a))

#variable names are case-sensitive