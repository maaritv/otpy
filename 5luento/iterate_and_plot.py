import math
import matplotlib.pyplot as plt

## Tutustu iteroivaan tapaan etsiä x, kun y:n arvo
## on annettu ja tiedetään ympyrän kaava.

def draw_plot(x, y):
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size
    plt.plot(x, y, '-+', label='circle area')  # Plot the sine curve
    plt.title('area')
    plt.xlabel('radius')
    plt.ylabel('circle area')
    plt.legend()  # Show legend
    plt.grid()  # Add grid lines
    plt.show()  # Display the plot

# Function to calculate the area of a circle given the radius
def calculate_circle_area(radius):
    return math.pi * math.pow(radius, 2)

# Function to find the radius using brute force iteration
def find_radius_for_area(target_area, start_from, step, precision, max_iterations):
    radius = start_from
    x=[]
    y=[]

    for i in range(max_iterations):
        area = calculate_circle_area(radius)
        if abs(area - target_area) <= precision:
            return (x,y)
        if area > target_area:
            if i == 0:
                raise ValueError("Try smaller start value!")
            raise ValueError("Could not find goal on given precision. Try to decrease the step value.")
        else:
            print(f"Iteration {i}: Tried r={radius} Result: {area}")

        x.append(radius)
        y.append(area)
        radius += step

# Usage
target_area = 34
start_from = 1
step = 0.01
precision = 0.1
max_iterations = 1000

try:
    (x,y) = find_radius_for_area(target_area, start_from, step, precision, max_iterations)
    area = calculate_circle_area(x[-1])
    print(f"Radius that produces a circle area of {target_area} is approximately: {x[-1]}")
    print(f"Area is then {y[-1]}")
    draw_plot(x,y)
except ValueError as e:
    print(f"Error: {e}")
