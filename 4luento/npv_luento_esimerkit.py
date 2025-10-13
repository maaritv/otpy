def calculate_npv_for_list(C, r):
    npv = 0.00
    #print(f"Investointi on {C[0]}")
    for t in range(0, len(C)):
        pv = C[t] / (1 + r) ** t
        print(f"Year: {t} PV of {C[t]} is {pv}")
        npv = npv + pv

    return npv


cash_flows = [-1000, 100, 200, 500, 300]
r = 0.05 # 5%

npv = calculate_npv_for_list(cash_flows, r)
print(f"Nykyarvo on {npv}")


def calculate_npv(C, r, n, initialInvestment):
    npv = 0.00
    for t in range(1, n):
        pv = C / (1 + r) ** t
        print(f"year: {t} PV of {C} is {pv}")
        npv = npv + pv
    npv = npv - initialInvestment
    return npv

yearly_income = 200
n=5 # Viisi vuotta (0, 1, 2, 3, 4)
investmentExpense = 1000  #ANNETAAN TÄSSÄ POSITIIVISENA, KAAVA VÄHENTÄÄ TÄMÄN.

npv = calculate_npv(yearly_income, r, n, investmentExpense);
print(f"Vakio {yearly_income} kokoisella vuositulolla investoinnin nykyarvo on {npv}")