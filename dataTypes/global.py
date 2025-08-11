x = "awesome"

def myFunc():

    print("Python is "+ x)
    y = "saksham"
myFunc()

#as x was defined outside the function therefore it is a global variable

# print(y) giving error because it is inside the function block and not globally declared

# to have a variable inside a function and still want it to be globally used, use global keyword

def saxuFunc():
    global z 
    z = "wah"


saxuFunc()
print(z)
