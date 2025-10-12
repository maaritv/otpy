import statistics

# Negatiivinen kovarianssi kertoo, että hinnat ja lämpötilat vaihtelevat vastakkaisiin 
# suuntiin, mutta arvosta ei voi päätellä kuinka vahvasti arvot vaihtelevat yhdessä.
# sitä varten pitäisi laskea korrelaatio.

electricity_prices_per_day=[55, 51, 40, 51, 35, 53, 49, 41, 49, 59, 60, 58, 62, 41, 45, 57, 49, 64, 57, 52]
outdoor_temperature_per_day=[18, 17, 16, 10, 8, 3, 1, 2, 1, -2, -1, -1, 5, 5, 5, 10, 13, 16, 13, 10]
covariance_temperature_and_electricity_prices = statistics.covariance(electricity_prices_per_day, outdoor_temperature_per_day)

print("Kovarianssi sähkön hinnan ja vastaavan ajanjakson lämpötilojen välillä on", '')
print(covariance_temperature_and_electricity_prices)

correlation = statistics.correlation(electricity_prices_per_day, outdoor_temperature_per_day)
print(f'Korrelaatio (arvot voivat olla välillä -1, 1) on pieni, eli negatiivinen yhteys on hyvin pieni. {correlation}')