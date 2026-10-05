from datetime import datetime


## TIEDOKSI! EI TARVITSE OPETELLA TEKEMÄÄN.
 

def create_hotel_booking(first_name, last_name, hotel_id):
    # Create a new booking object with the given details
    booking = {
        "first_name": first_name,
        "last_name": last_name,
        "hotel_id": hotel_id,
        "booking_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return booking



try:
    # Koodin suoritus alkaa tästä
    ## Koska tarkastukset voivat antaa poikkeuksen, pitää nämä rivit 
    ## määritellä try – except -lohkon sisällä, muuten koodi “kaatuu” eli
    ## päättyy hallitsemattomasti.
    # Pyydetään syöte käyttäjältä (käyttöliittymäkerros)
    first_name = input("Enter your first name: ")
    ##Syötteen validointi!
    if not isinstance(first_name, str) or not first_name.strip() or not first_name.isalpha():
        raise ValueError("First name must be a non-empty string.") 

    last_name = input("Enter your last name: ")
    if not isinstance(last_name, str) or not last_name.strip() or not last_name.isalpha(): 
        raise ValueError("Last name must be a non-empty string.") 

    # Validate hotel_id to be an integer 

    hotel_id = input("Enter the hotel ID: ")
    if not isinstance(int(hotel_id), int): 
        raise ValueError("Hotel ID must be an integer.")

    # Create the booking
    booking = create_hotel_booking(first_name, last_name, hotel_id)

    # Print the booking details
    print("Booking created successfully:")
    print(booking)

except ValueError as e:
    print(f"Booking was not created, because of invalid input from the user {e}.")

