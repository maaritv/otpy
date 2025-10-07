
## TIEDOKSI! EI TARVITSE OPETELLA TEKEMÄÄN.

# 1) Funktio saa parametrin, joka voi muuttua joka ajokerralla
def process_data(data):
    print(f"Käsittelen dataa: {data}")

# 2) Asiakastietojen tallennus
def save_customer(customer_data):
    print(f"Tallennetaan asiakas: {customer_data}")
    # Tässä voisi olla tietokantatallennus

# 3) Putoamiskiihtyvyyden laskeminen (mgh)
def potential_energy(m, h):
    g = 9.81  # vakio, ei parametrina
    return m * g * h

# --- Esimerkkikäyttö ---
process_data({"name": "Testi", "age": 30})
save_customer({"id": 123, "name": "Matti Meikäläinen"})
print("Potentiaalienergia:", potential_energy(5, 10))
