import numpy as np
import matplotlib.pyplot as plt


rate = 0.1
cashFlows = [-1000, 200, 300, 400, 500]
x = []
y = []


for t in range(0, len(cashFlows)):
  y.append((1 + rate) ** t)
  x.append(t)

# Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, label='Curve')  # Plot the curve
plt.title('Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()  # Show legend
plt.grid()  # Add grid lines
plt.show()  # Display the plot
