names = ['Matti', 'Minna', 'Iines', 'Joni', 'Mikko', 'Leena']

name = "Alkuperäinen arvo"
for i in range(len(names)):
    #Tämä name muuttuja on sama kuin 3-rivillä määritelty
    #eikä eri muuttuja kuten varjostus edellyttäisi. 
    #Siten varjostusta EI tapahdu tässä.
    name = names[i]
    print(name)

# Tämä toimii, koska name-muuttuja säilyttää viimeisimmän arvon for-loopin jälkeen.
print(f'Nimet loppuivat. Name muuttujan arvo nyt {name} ja i oli viimeksi {i}')
