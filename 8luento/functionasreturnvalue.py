def outer_function():
    def inner_function():
        print("Inner function!")
    return inner_function

func = outer_function()  # func now holds inner_function
func()  # Outputs: Inner function!
