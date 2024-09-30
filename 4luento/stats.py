import statistics

#Älä anna samaa nimeä koodimodulille kuin
#on kirjastolla!

values = [23.98, 67.34, 986.87, 372.88, 372.88, 4.0, 7.9]

average = statistics.mean(values)
print(f"Keskiarvo on {average}")

median = statistics.median(values)
print(f"Mediaani on {median}")

stdev = statistics.stdev(values)
print(f"Keskihajonta on {stdev}")

