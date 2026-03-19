import matplotlib.pyplot as plt

def main():
    """
    Problem:
    Create a pie chart showing a company's market share relative to its competitors.
    Explode the slice representing the company itself to highlight it.
    Format the slice labels to show percentages.
    """
    labels = ['Our Company', 'Competitor A', 'Competitor B', 'Competitor C', 'Others']
    sizes = [35, 25, 20, 15, 5]
    
    # Explode the first slice ('Our Company')
    explode = (0.1, 0, 0, 0, 0)
    
    # Custom colors
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    plt.figure(figsize=(7, 7))
    
    # Plotting the pie chart
    wedges, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                       autopct='%1.1f%%', shadow=True, startangle=140)
                                       
    # Styling text inside pie
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')
        
    plt.title('Market Share Breakdown - Q3 2024', fontweight='bold', pad=20)
    
    # Ensure drawing is circular
    plt.axis('equal')  
    plt.show()

if __name__ == "__main__":
    main()
