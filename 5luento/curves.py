import numpy as np
import matplotlib.pyplot as plt

## Tämä ohjelmakoodi tiedoksi.

## Asenna: pip3 install matplotlib
## pip3 install numpy

## Sovellus avaa graafisen ikkunan, joten 
## Macissa ja Windowwssissa ohjelmaa pitää ajaa sen käyttäjän
## oikeuksilla, jolla on graafinen istunto koneeseen.
## Linuxissa voit käyttää xhost + -komentoa ja 
## avata ikkunoita myös toisen käyttäjän graafiseen 
## ikkunaan. 

x = np.linspace(-6, 2, 500)

##y = np.sqrt(x)
#x = 3.45  # Laske y:n arvo tietyllä x:n arvolla
y = (x**2) + (4 * x) - 5

# Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, label='Curve')  # Plot the curve
plt.title('Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()  # Show legend
plt.grid()  # Add grid lines
plt.show()  # Display the plot
