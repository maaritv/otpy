import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 1000)
# Calculate the corresponding y values using the sine function
y = np.sin(x)
# Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, label='sin(x)')  # Plot the sine curve
plt.title('Sine Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()  # Show legend
plt.grid()  # Add grid lines
plt.show()  # Display the plot
