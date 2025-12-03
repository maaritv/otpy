import copy

def get_formula_for_greetings(customer):
    # Tarkistetaan parametrit kuten JS-versiossa
    if not customer or "age" not in customer or "name" not in customer:
        raise ValueError("Customer parameter or age field was missing.")

    # Sisäfunktioiden ulkopuolelle jäävä customer tallentuu sulkeumaan (closure)
    # Syväkopio tehdään kuten JS:ssä
    def say_bye():
        my_customer = copy.deepcopy(customer)
        print(f"I am sorry {my_customer['name']}, but you are too young to use this app.")

    def say_hi():
        my_customer = copy.deepcopy(customer)
        print(f"Hi, Welcome {my_customer['name']}")

    if customer["age"] < 10:
        return say_bye
    else:
        return say_hi


# Testidata
maija = {
    "name": "Maija",
    "age": 9
}

matti = {
    "name": "Matti",
    "age": 19
}

# Funktiot
formula_for_greetings_to_maija = get_formula_for_greetings(maija)
formula_for_greetings_to_matti = get_formula_for_greetings(matti)

# Kutsut
formula_for_greetings_to_matti()
formula_for_greetings_to_maija()
