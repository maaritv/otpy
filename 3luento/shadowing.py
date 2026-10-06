# global variable
a = 3

def printA():

    # local variable
    a = 5
    print(a)  # prints 5

printA()
print(a)  # prints 3