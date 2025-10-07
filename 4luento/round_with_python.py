from math import *


## TIEDOKSI! EI TARVITSE OPETELLA TEKEMÄÄN.

a = 34.22  # 4 merkitsevää numeroa, 2 desimaalia
b = 91.76627773  #10 merkitsevää numeroa
c = a * b
precision = 4

rounded_c = '{:g}'.format(float('{:.{p}g}'.format(c, p=precision)))
print(
    f"c pyöristettynä 4:n merkitsevän numeron tarkkuudella is {rounded_c} its type is {type(c)}"
)
print('{:g}'.format(float('{:.{p}g}'.format(c, p=4))))

d = a + b
print(f"Tulosta kahden desimaalin tarkkuudella {round(d, 2)}")
