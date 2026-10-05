

#Testaa erilaisilla syötteillä.
# python3 calculate_area.py


def calculate_rectangle_area(width, height):
    #Esiehtotarkistus
    if (width < 0):
        raise ValueError("Leveyden pitää olla positiivinen numero")
    if (height < 0):
        raise ValueError("Korkeuden pitää olla positiivinen numero")

    area = width * height
    return area


widthInput= "120"  #Leveys on teknisesti ottaen merkkijono, mutta se on muunnettavissa numeroksi.
heightInput = 13

try:
    #Syötevalidointi (ei-tyhjä, numeerinen tietotyyppi)
    if (widthInput is None or (str(widthInput)).isnumeric() == False):
        raise TypeError("Leveyden pitää olla numero")
    if (heightInput is None or (str(heightInput)).isnumeric() == False):
        raise TypeError("Korkeuden pitää olla numero")
    # Muutetaan syötteet kokonaisluvuiksi
    width = int(widthInput)
    height = int(heightInput)
    area = calculate_rectangle_area(width, height)
    print(f"Pinta-ala on {area}")
except ValueError as value_error:
    print(f"Esiehtotarkistus epäonnistui: Pinta-alan pitää olla positiivinen numero. {value_error}\n\n")
except TypeError as type_error:
    print(f"Syötevalidointi epäonnistui: Pinta-ala lasketaan numeroista. {type_error}\n\n")
