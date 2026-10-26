import matplotlib.pyplot as plt

def calculate_energy(P):
    # Lasketaan kokonaisenergia
    E = sum(P)
    return E

def calculate_energy_in_loop(P, sampling_period_s):
    # Prosessorin teho watteina
    # Lasketaan kokonaisenergia for-silmukalla
    E = 0
    #print(f"Using sampling period {sampling_period_s} seconds")

    for t in range(len(P)):
        E = E + P[t] * sampling_period_s #jos mitataan sekunnin välein tämä on 1
    return E

def draw_diagram(P):
    energia = 0
    kulutus = [0]

    for teho in P:
        energia += teho
        kulutus.append(energia)

    plt.plot(range(12), kulutus)
    plt.xlabel("Aika (s)")
    plt.ylabel("Energia (J)")
    plt.title("Prosessorin energiankulutus")
    plt.grid()
    plt.show()


# Prosessorin teho watteina sekunnin välein
P = [51, 71, 74, 70, 69, 0.17, 0, 74, 68, 70, 70]
E1 = calculate_energy(P)
E2 = calculate_energy_in_loop(P, 1)

# Tulostetaan tulos
print(f"Prosessorin kuluttama energia on {E1} vs. {E2} joulea.")

#Twhoarvot mitattu puolen sekunnin välein
P2 = [51, 52, 71, 70, 74, 73, 70, 69, 0.17, 0.90, 74, 68, 70, 70, 40, 32, 18, 19, 80, 98, 70, 71]
print(len(P2))
E3=calculate_energy_in_loop(P2, 0.5)
print(f"Prosessorin kuluttama energia, kun teho mitataan 2 kertaa sekunnissa on {E3} Joulea.")

#draw_diagram(P)

