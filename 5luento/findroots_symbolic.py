from sympy import *

## Ratkaisee x:n arvon, jolla y:n arvoksi tulee 0


def find_zeros():
  x, y = symbols('x y')
  y = (x**2) + (4 * x) - 5
  result = solve(y)
  return result


zeros = find_zeros()
print(f"Nollakohdat {zeros}")
