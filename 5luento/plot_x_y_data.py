import math
import matplotlib.pyplot as plt


# Harjoittele kuvaajien piirtämistä. Tutustu matplot-lib:n mahdollisuuksiin 
# sen API:n kautta.
# https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

def draw_plot(x, y):
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size
    plt.plot(x, y, '-+', label='Suklaan hinnanvaihtelu')  # Plot the sine curve
    plt.title('Suklaan kuukausittainen keskihinta / kilo vuoden aikana')
    plt.xlabel('kuukausi')
    plt.ylabel('hinta (euroa)')
    plt.legend()  # Show legend
    plt.grid()  # Add grid lines
    plt.show()  # Display the plot



x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [8.00, 8.50, 8.70, 11.50, 10.50, 9.50, 5.90, 5.90, 6.00, 6.10, 7.90, 12.30]

draw_plot(x, y)


