import math

a = 1.2
b = 4
c = a + b

print(c)
print(f"A:n tyyppi {type(a)} B:n tyyppi {type(b)}. C:n tyyppi {type(c)}.")


#Bittitason vastaavuus (täydellinen vastaavuus)
claim  = 0.1 + 0.2 == 0.30000000000000004
print(0.1+0.2)
print(f"Tämä väite on {claim}") 

claim = math.isclose((0.1+0.2), 0.3)
print(f"Nyt tämä väite on {claim}") 