def greet():
    print("Hello!")

def farewell():
    print("Goodbye!")

# Storing functions in a list
actions = [greet, farewell]

# Iterating and calling the functions
for action in actions:
    action()  # Outputs: Hello! Goodbye!
