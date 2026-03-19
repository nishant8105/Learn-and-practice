import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Problem:
    Create a bar chart showing the sales revenue of 5 different product categories.
    Add data labels on top of each bar so the exact values can be read easily.
    """
    categories = ['Electronics', 'Clothing', 'Home', 'Toys', 'Sports']
    revenue = [45000, 28000, 32000, 15000, 21000]

    plt.figure(figsize=(8, 5))
    
    # Create colors for each bar
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # Plotting the bar chart
    bars = plt.bar(categories, revenue, color=colors, edgecolor='black')
    
    # Adding titles and labels
    plt.title('Annual Revenue by Product Category')
    plt.xlabel('Category')
    plt.ylabel('Revenue ($)')
    
    # Adding data labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 500, f'${yval}', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
                 
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
