
# aja sovellus terminaalissa komennolla:
# python3 inputvalidationexample.py


#Funktio laskee suorakulmion pinta-alan
# Esiehtotarkastuksessa se tarkistaa, että pinta-alasta
# pitää tulla positiivinen luku.
def calculate_rectangle_area(width, height):
    if (width * height) < 0:
        raise ValueError("Pinta-ala ei voi olla negatiivinen!")
    return (width * height)

def calculate_area():
    # Get input values from user input
    try:
        width_input = input("Syötä leveys? ")
        length_input = input("Syötä pituus? ")
        ##Tyyppimuunnos antaa poikkeuksen, jos muunnos ei onnistu
        ##JavaScriptissä näin ei käy
        width = float(width_input)
        length = float(length_input)
        
        ##Tässä kohdassa Python toimii eri tavoin kuin JavaScript, ja systemaattinen
        ## muuntaminen ei tuota toimivaa koodia.
        # If width or length cannot be converted to a number, raise an exception
        ##if width <= 0 or length <= 0:
        ##    raise ValueError("Syötettä ei voitu muuntaa numeroksi")
        
        result = calculate_rectangle_area(width, length)
        print(f"Pinta-ala on: {result}")
    except ValueError as error:
        print(f"Pinta-alaa ei voitu laskea: {error}")

# Call the calculate_area function
calculate_area()
