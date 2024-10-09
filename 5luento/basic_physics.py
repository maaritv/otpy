# Tämä laskin osaa laskea yhteen, vähentää ja
# laskea keskiarvon kahdesta muuttujasta


def calculate_sum(param1, param2):
  summa = param1 + param2
  return summa


def calculate_difference(param1, param2):
  diff = param1 - param2
  return diff


def calculate_average(param1, param2):
  summa = calculate_sum(param1, param2)
  return summa / 2


## If numbers are equal returns 0
def find_biggest_number(param1, param2):
  if param1 == param2:
    return 0
  if param1 > param2:
    return param1
  else:
    return param2


def calculate_circle_area(r):
  pi = 3.14
  area = pi * (r * r)
  return area


## Funktioon on lisätty tarkistus, jotta argumentit ovat
## numeerisia eikä pinta-alasta tule negatiivistä.
## python on dynaamisesti tyypitetty kieli, joten kääntäjää
## ei ole antamassa virhettä, jos kutsuva funktio antaa
## argumentit väärässä tyypissä.
## Tässä kuitenkin kelpaavat molemmat numeeriset tietotyypit.
## float ja int


def calculate_rectange_area(width, height):
  if (width is None or (str(width)).isnumeric() == False or width < 0):
    raise ValueError("Leveyden pitää olla positiivinen numero")
  if (height is None or (str(height)).isnumeric() == False or height < 0):
    raise ValueError("Korkeuden pitää olla positiivinen numero")
  area = width * height
  return area


## P = UI
def calculate_power(u, i):
  p = u * i
  return p


# Ohjelman suoritus alkaa. Voidaan kutsua yllämääriteltyjä
# funktioita.

eka = 120
toka = 13

area = calculate_rectange_area(eka, toka)
print(f"Pinta-ala on {area}")
sum_result = calculate_sum(eka, toka)
# print("Summa on "+result)
sum_result_str = str(sum_result)
print("Sum_str_result tietotyyppi on " + str(type(sum_result_str)))
print("Summa on " + sum_result_str + "\n\n")

diff_result = calculate_difference(8, 3)
print("diff_result tietotyyppi on " + str(type(diff_result)))
print("Erotus on " + str(diff_result) + "\n\n")

average_result = calculate_average(4, 9)
print("average_result tietotyyppi on " + str(type(average_result)))
print("Keskiarvo on " + str(average_result) + "\n\n")

bigger_number = find_biggest_number(800, 7000)
print("Bigger number is " + str(bigger_number))

print("Hei " + str(average_result) + " " + "kukkuu")

small_circle = calculate_circle_area(10)
big_circle = calculate_circle_area(200)
total_area = calculate_sum(big_circle, small_circle)

total_area = big_circle + small_circle

virta = 200
jannite = 300

teho = calculate_power(jannite, virta)
print("Teho on " + str(teho))
