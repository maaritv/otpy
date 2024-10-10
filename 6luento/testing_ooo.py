from Aircraft import Aircraft
from Airport import Airport
from Flight import Flight
import sys
import validations

# Save new flight saa parametrikseen nyt vain yhden lento objektin.
# Tämä objekti pitää sisällään kaiken tiedon mikä lentoon liittyy.
##
## Funktio palauttaa 1, jos tallennus onnistui
## 0 jos tallennus epäonnistui
## -1 jos validointi epäonnistui

def save_new_flight(my_flight):
  print(
    "Aivan ensin tässä kuuluu tarkistaa jokainen parametri, että ne edustavat järkevää tietotyyppiä ja ovat loogisestikin järkeviä. Esim. ei voida lisätä lentoa, jonka maksimimatkustajamäärä on negatiivinen numero."
  )
  my_flight.invariant()
  print(
    "Kun olet käynyt Database programming kurssin, tiedät miten tämä funktio toteutetaan niin, että lento lisätään pysyvään säilöön (persists), kunnes joku muu tarvitsee sitä."
  )
  return 0


## Koodin suoritus alkaa tästä ##
try:
  flight_aircraft_type = input("Anna lentokoneen merkki ja malli ")
  validations.validateNotEmpty(flight_aircraft_type)
  flight_aircraft_max_passagers = input(
    "Montako matkustajaa koneeseen mahtuu ")
  validations.validateNumber(flight_aircraft_max_passagers)
  flight_airport_from_name = input("Anna lähtölentoaseman koodi (XXX) ")
  validations.validateAirportCode(flight_airport_from_name)
  flight_start_time_zone = input("Anna lähtöajan aikavyöhyke (+/- II) ")
  validations.validateTimezone(flight_start_time_zone)
  flight_airport_to_name = input("Anna kohdelentoaseman koodi (XXX) ")
  validations.validateAirportCode(flight_airport_to_name)
  flight_end_time_zone = input("Anna saapumisaikavyöhyke ")
  validations.validateTimezone(flight_end_time_zone)
  flight_no = input("Anna lennon numero ")
  validations.validateNumber(flight_no)
  flight_start_time = input("Lennon lähtöaika (HH:mm) ")
  validations.validateTime(flight_start_time)
  flight_end_time = input("Lennon saapumisaika (HH:mm) ")
  validations.validateTime(flight_end_time)
  flight_start_date = input("Anna lähtöpäivä (YYYY-MM-DD) ")
  validations.validateDate(flight_start_date)
  flight_end_date = input("Anna tulopäivä (YYYY-MM-DD) ")
  validations.validateDate(flight_end_date)
  flight_ticket_price = input("Lennon hinta euroina ")
  validations.validateNumber(flight_ticket_price)
  ##Time stamp muuttuja sisältää merkkijonon, johon sisältyy sekä päivämäärä että kellonaika 2023-04-18 07:32:05.289406+00:00
  flight_start_timestamp = f"{flight_start_date} {flight_start_time}:00.000"
  flight_end_timestamp = f"{flight_end_date} {flight_end_time}:00:000"

  ## Luodaan luokat.

  aircraft = Aircraft(flight_aircraft_type, flight_aircraft_max_passagers)
  from_airport = Airport(flight_airport_from_name, flight_start_time_zone)
  to_airport = Airport(flight_airport_to_name, flight_end_time_zone)

  ## Lento siältää lentokoneen ja kaksi lentoasemaa. Tässä muodostuu 
  ## luokkien välinen hierarkia. Josta tietokannassa tulee relaatio 
  ## lennon, lentokoneen, ja lentoasemien välille.
  myflight = Flight(flight_start_timestamp, flight_end_timestamp, flight_no,
                  aircraft, from_airport, to_airport, flight_ticket_price)

  
  print("tuotot lennosta ", myflight.calculate_maximum_ticket_profit())

  myflight_database_id = save_new_flight(myflight)
  print(
  "Lento on lisätty systeemiin, nyt voit alkaa lisätä sille matkustajia. Sen koodi on ",
  myflight_database_id)

except ValueError as e:
  print(f"Virhe syötetiedoissa! {e}")