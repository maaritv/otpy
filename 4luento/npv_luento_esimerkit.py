def calculate_npv_for_list(C, r):
    if (r<0 or r>100):
        raise ValueError(f"Interest rate must be between 0 and 100%!")
    if (len(C)<0):
        raise ValueError(f"Number of years must be positive!")
    if (C[0]>0):
        raise ValueError(f"Investment must be negative!")
    npv = 0.00
    #print(f"Investointi on {C[0]}")
    for t in range(0, len(C)):
        pv = C[t] / (1 + r) ** t
        print(f"Year: {t} PV of {C[t]} is {pv}")
        npv = npv + pv

    return npv


def calculate_npv(C, r, n, initialInvestment):
    if (C<0):
        raise ValueError(f"Yearly cash flows must be positive!")
    if (r<0 or r>100):
            raise ValueError(f"Interest rate must be between 0 and 100%!")
    if (n<0):
            raise ValueError(f"Number of years must be positive!")
    if (initialInvestment>0):
        raise ValueError(f"Investment must be negative!")
    
    npv = 0.00
    for t in range(1, n):
        pv = C / (1 + r) ** t
        print(f"year: {t} PV of {C} is {pv}")
        npv = npv + pv
    npv = npv + initialInvestment
    return npv


yearly_income = input("Vuosittainen tuotto (€)") #200
n=input("Investoinnin taloudellinen pitoaika (v): ") #5 # Viisi vuotta (0, 1, 2, 3, 4)
investmentExpense = input("Investointikustannus, joka maksetaan ensimmäisenä vuonna (€): ") #-1000  
r=input("Riskitön pankkitalletuksen korkoprosentti: ")

npv = calculate_npv(int(yearly_income), float(r)/100, int(n), int(investmentExpense));
print(f"Vakio {yearly_income} kokoisella vuositulolla investoinnin nykyarvo on {npv}")

cash_flows = [-1000, 200, 200, 200, 200]

npv = calculate_npv_for_list(cash_flows, float(r)/100)
print(f"Nykyarvo on {npv}")