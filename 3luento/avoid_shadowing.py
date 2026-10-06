# global variable
a = 3

def printA():
    # Tell that variable a is global
    # local a -variable can be created.
    # global and nonlocal avainsanat toimivat vain funktio-lohkossa
    # niillä ei voi hallita varjostusta muissa lohkoissa.
    global a
    # local variable
    a = 5
    print(a)  # prints 5

printA()
print(a)  # prints 3