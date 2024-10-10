class Airport:

  def __init__(self, airport_name, timezonestr):
    print("2. Initialize the new instance of Airport.")
    self.name = airport_name
    self.timezonestr = timezonestr

  def __repr__(self) -> str:
    return f"{type(self).__name__}(name={self.name}, timezonestr={self.timezonestr})"

  def invariant(self):
    print(
      "Tarkastusta ei ole toteutettu vielä. Tarkista että sekä nimi että aikavyöhyke on annettu."
    )
