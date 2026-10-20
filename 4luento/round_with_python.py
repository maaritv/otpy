from math import *


## TIEDOKSI! EI TARVITSE OPETELLA TEKEMÄÄN.

a = 34.22  # 4 merkitsevää numeroa, 2 desimaalia
b = 91.76327773  #10 merkitsevää numeroa

c = a * b
d=b-a

precision_c = 0 #kertolaskun tuloksen desimaaleja on 0, koska tulokseen 4 merkitsevää lukua. (3140)
precision_d=2  #a on epätarkempi, kaksi desimaalia (vähennyslasku)

rounded_c = int(c)
rounded_d=round(d, precision_d)



print(
    f"c {c} pyöristettynä 4:n merkitsevän numeron tarkkuudelle on {rounded_c}. Koska tulos on yli tuhat, pyöristetään kokonaisluvuksi.\n{rounded_c} its type is {type(c)}"
)

print(f"d {d} pyöristettynä neljän desimaalin tarkkuudelle {rounded_d}")
