from sympy import *
import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial
def solve_numerically():
  coeffs = [1, -3, 0, 2]
  y = np.array(coeffs)
  #tarkoittaa polynomia x^3 - 3x^2 + 0x + 2
  roots = np.roots(y)
  ##print(f"Juuret ovat {roots}")
  return roots


#Esimerkki 2.15
#etsi polynomin nollakohdat
#http://www.math.jyu.fi/matyl/propedeuttinen/kirja/index-36.html


def algebraic_solution():
  x, y = symbols('x y')
  y = (x**3) - (3 * x**2) + 2
  result = solve(y)
  return result



algebraic_solution = algebraic_solution()
numerical_solution = solve_numerically()
print(f"Algebrallinen ratkaisu {algebraic_solution}")
print(f"Numeerinen ratkaisu {numerical_solution}")
