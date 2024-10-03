import math

#Lasketaan kertoma.
#https://fi.wikipedia.org/wiki/Permutaatio

#Ilman matematiikkafunktiota
#esim. n = 3
# 3 x 2 x 1


def calculate_factorial(n):
  if n<0:
    raise ValueError("Factorial for negative value is not defined.")
  tmp = 1
  for i in reversed(range(1, n + 1)):
    tmp = i * tmp  ## tmp muuttuja ei ole kertoma
  factorial = tmp
  return factorial  #viimeisin arvo on oikea vastaus


n = -4
print(f"{n} palloa voidaan laittaa {calculate_factorial(n)} järjestykseen")

fact=math.factorial(n)

print(f"{n} palloa voidaan laittaa {fact} järjestykseen")
