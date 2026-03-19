import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Problem:
    Create a line plot comparing the average monthly temperatures of two cities 
    over a year. Add appropriate labels, title, a legend, and a grid.
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Temperature data in Celsius
    city_a_temps = [5, 7, 12, 18, 22, 26, 29, 28, 24, 18, 11, 6]
    city_b_temps = [15, 16, 18, 20, 23, 25, 27, 28, 26, 23, 19, 16]

    plt.figure(figsize=(10, 6))
    
    # Plotting both lines
    plt.plot(months, city_a_temps, marker='o', linestyle='-', color='b', label='City A')
    plt.plot(months, city_b_temps, marker='s', linestyle='--', color='r', label='City B')
    
    # Adding titles and labels
    plt.title('Average Monthly Temperatures: City A vs City B')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    
    # Adding legend and grid
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
