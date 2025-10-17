import numpy as np
import matplotlib.pyplot as plt


#Harjoitus: Aja tämä tiedosto debug-työkalulla ja 
#suorita katkoskohdasta (break point) lähtien ohjelmakoodia
#rivi kerrallaan.


# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 1000)
# Calculate the corresponding y values using the sine function
y = np.sin(x)

# x ja y ovat tässäkin nyt listoja numeroita.
print(x)

print(y)


# Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, label='sin(x)')  # Plot the sine curve
plt.title('Sine Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()  # Show legend
plt.grid()  # Add grid lines
plt.show()  # Display the plot
