import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Problem:
    Create a scatter plot demonstrating the relationship between study hours 
    and exam scores. Map the size of the points to a third variable (e.g., student confidence level)
    and use a colormap to indicate the score intensity.
    """
    # Generate mock data
    np.random.seed(42)
    study_hours = np.random.uniform(1, 10, 50)
    # Scores have a positive correlation with study hours + some noise
    exam_scores = (study_hours * 8) + np.random.normal(10, 10, 50) 
    exam_scores = np.clip(exam_scores, 0, 100) # Keep scores between 0 and 100
    
    # Confidence level from 1 to 10 mapped to point scale (size)
    confidence = np.random.uniform(1, 10, 50)
    point_sizes = confidence * 20

    plt.figure(figsize=(9, 6))
    
    # Plotting the scatter plot
    scatter = plt.scatter(study_hours, exam_scores, s=point_sizes, c=exam_scores, 
                          cmap='viridis', alpha=0.7, edgecolors='w', linewidth=0.5)
    
    # Adding color bar for the score intensity
    cbar = plt.colorbar(scatter)
    cbar.set_label('Exam Score Intensity')
    
    # Adding titles and labels
    plt.title('Study Hours vs. Exam Score\n(Bubble Size = Confidence Level)')
    plt.xlabel('Hours Studied')
    plt.ylabel('Exam Score (%)')
    
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()
