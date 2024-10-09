import matplotlib.pyplot as plt

## Harjoitustehtävässä tehtävänä lisätä esiehtotarkastus 
## myös tähän Python-versioon. Korkotason pitää olla positiivinen.

def calculate_npv(rate, cash_flows):
  npv = 0
  for i, cash_flow in enumerate(cash_flows):
    present_value = cash_flow / (1 + rate)**i
    npv = npv + present_value
  return npv



## KOODIN SUORITUS ALKAA TÄSTÄ
interest = 0.1 ## 1 prosentin riskitön korko pankkitalletukselle.
yearly_net_cash_flows = [-1000, 200, 300, 400, 500];
npv = calculate_npv(interest, yearly_net_cash_flows)
print(
    f"Vuosittain vaihtelevien kassavirtojen nykyarvo (investoinnin tuotto) on: {npv}"
)

fig, ax = plt.subplots()
ax.plot(range(0, len(yearly_net_cash_flows)), yearly_net_cash_flows)
plt.ylabel('Vuosittaiset vaihtelevat kassavirrat')
plt.show()
