import statistics

electricity_prices_per_day=[4, 8, 8, 8, 4, 10, 12, 18, 22, 22, 23, 24]
outdoor_temperature_per_day=[24, 18, 17, 16, 10, 8, 3, 1, 2, 1, -2, -1]
covariance_temperature_and_electricity_prices = statistics.covariance(electricity_prices_per_day, outdoor_temperature_per_day)

print("Kovarianssi sähkön hinnan ja vastaavan ajanjakson lämpötilojen välillä on", '')
print(covariance_temperature_and_electricity_prices)
