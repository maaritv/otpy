## Flight-luokka.


class Flight:

  ## Rakentaja
  def __init__(self, flight_start_timestamp, flight_end_timestamp, flight_no,
               aircraft, start_airport, destination_airport,
               flight_ticket_price):
    print("2. Initialize the new instance of Flight.")
    ##rakentaja alustaa jäsenmuuttujat.
    self.starts_timestamp = flight_start_timestamp
    self.ends_timestamp = flight_end_timestamp
    self.flight_no = flight_no
    self.aircraft = aircraft
    self.start_airport = start_airport
    self.destination_airport = destination_airport
    self.flight_ticket_price = flight_ticket_price

  def __repr__(self) -> str:
    return f"{type(self).__name__}(flight_no={self.flight_no}, start_airport={self.start_airport})"

  ## Jäsenfunktio
  ## Maksimi lennon tuotto saadaan kertomalla
  ## lentokonekohtainen maksimimatkustajamäärä
  ## lennon hinnalla.
  def calculate_maximum_ticket_profit(self):
    return int(self.aircraft.max_number_of_passangers) * int(
      self.flight_ticket_price)

  def checkStartAndEndTimestamps(self):
    ## Muunna aikaleimoiksi ja vertaa, että ne ovat vasta tulevaisuudessa sekä keskenään oikeassa
    ## järjestyksessä. Jos eivät ole, anna poikkeus.
    print(
      "Tarkastusta ei ole toteutettu vielä. tarkista, että lähtöaika ja saapumisaika ovat vasta tulevaisuudessa ja keskenään oikeassa järjestyksessä!"
    )

  def invariant(self):
    self.checkStartAndEndTimestamps()
    ##Lisätarkistukset myös muille lennon jäsenmuuttujille että ne on annettu
    self.checkAirports()
    self.start_airport.invariant()
    self.destination_airport.invariant()
    self.aircraft.invariant()

  def checkAirports(self):
    ##Tarkista jäsenmuuttujista start_airport ja destination_airport
    if (self.start_airport.name == self.destination_airport.name):
      raise ValueError("Lähtöasema ja kohdeasema eivät saa olla samat!")
