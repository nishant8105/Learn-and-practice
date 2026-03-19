import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Problem:
    Create a histogram showing the distribution of human heights in a population.
    Plot a vertical line representing the mean height.
    """
    # Generate mock normally distributed human heights (in cm)
    np.random.seed(0)
    # Mean = 170cm, Std Dev = 10cm, Sample size = 1000
    heights = np.random.normal(170, 10, 1000)
    
    mean_height = np.mean(heights)

    plt.figure(figsize=(8, 6))
    
    # Plotting the histogram
    # Using 30 bins for good granularity
    plt.hist(heights, bins=30, color='skyblue', edgecolor='black', alpha=0.8)
    
    # Highlighting the mean line
    plt.axvline(mean_height, color='red', linestyle='dashed', linewidth=2, 
                label=f'Mean Height: {mean_height:.1f} cm')
    
    # Adding titles and labels
    plt.title('Distribution of Human Heights')
    plt.xlabel('Height (cm)')
    plt.ylabel('Frequency / Number of People')
    
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    
    plt.show()

if __name__ == "__main__":
    main()
