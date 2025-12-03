
# Python exporttaa funktion automaattisesti, jos 
# sen nimi ei ala _:lla.

def validate_number(s):
    try:
        float(s)
    except ValueError:
        raise TypeError("Merkkijonon pitää olla numeroarvo.")
