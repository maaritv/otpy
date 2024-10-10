##Syötevalidointi!!!


def validateNotEmpty(strng):
  if (len(strng) == 0):
    raise ValueError("Merkkijono pitää antaa")

##Tarkista lentoaseman tiedot, jotta nimi on annettu koodina, jolla asema on helppoa hakea tietokannasta
def validateAirportCode(name):
  validateNotEmpty(name)
  if (len(name) != 3):
    raise ValueError('Letnoaseman koodin pitää olla 3 merkkiä pitkä!')


## Aikavyöhykkeen pitää ensinnäkin olla olemassa. Huomaa, että tässä kutsutaan toista validaattoria, EI kopioida koodia.
def validateTimezone(timezone):
  validateNotEmpty(timezone)
  if (timezone.startswith("+") == False and timezone.startswith("-") == False):
    raise ValueError('Aikavyöhykeen pitää olla muodossa +/-numero.')


def validateNumber(nbr):
  validateNotEmpty(nbr)
  if (nbr.isnumeric() == False):
    raise ValueError("Pitää olla numero")


def validateTime(tme):
  print("todo: tarkista aikaformaatti!")


def validateDate(dte):
  print("todo: tarkista pvm formaatti!")
