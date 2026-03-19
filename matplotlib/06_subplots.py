import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Problem:
    Create a 2x2 grid of subplots containing 4 different mathematical functions:
    1. Sine wave
    2. Cosine wave
    3. Tangent wave (bounded)
    4. Exponential function
    Give each subplot its own title and customized line style.
    """
    # Create sample points
    x = np.linspace(0, 2 * np.pi, 100)
    
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(x/3) # Scaled exponential so it fits nicely

    # Set up 2x2 plot matrix
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Mathematical Functions Subplots', fontsize=16, fontweight='bold')

    # 1. Sine Wave (Top Left)
    axs[0, 0].plot(x, y1, color='blue', linestyle='-')
    axs[0, 0].set_title('Sine Wave')
    axs[0, 0].grid(True)

    # 2. Cosine Wave (Top Right)
    axs[0, 1].plot(x, y2, color='green', linestyle='--')
    axs[0, 1].set_title('Cosine Wave')
    axs[0, 1].grid(True)

    # 3. Tangent Wave (Bottom Left)
    # Bound the y axis for tangent so it doesn't skew to infinity
    axs[1, 0].plot(x, y3, color='red', linestyle='-.')
    axs[1, 0].set_ylim(-5, 5)
    axs[1, 0].set_title('Tangent Wave')
    axs[1, 0].grid(True)

    # 4. Exponential (Bottom Right)
    axs[1, 1].plot(x, y4, color='purple', linestyle=':')
    axs[1, 1].set_title('Exponential Function')
    axs[1, 1].grid(True)

    # Adjust layout so titles don't overlap
    plt.tight_layout()
    # Adding some space at the top for the main title
    fig.subplots_adjust(top=0.9) 
    
    plt.show()

if __name__ == "__main__":
    main()
