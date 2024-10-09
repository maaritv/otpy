
def find_zero_points():
    y = (4 * x**3) + (2 * x**2) - (12 * x) -20
    x=-100
    while true:
        if y<0:
            x=x+0.5
        else if y>0:
            x=x-0.5
        else
            print(f"Nollakohta löytyi x=", x)
            break;

find_zero_points()
