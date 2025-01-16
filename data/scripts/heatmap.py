import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_heatmap(cooccurrence_file, output_file):
    """
    Visualize the co-occurrence matrix as a heatmap.

    Args:
        cooccurrence_file (str): Path to the co-occurrence matrix CSV.
        output_file (str): Path to save the heatmap image.
    """
    # Load co-occurrence data
    cooccurrence_df = pd.read_csv(cooccurrence_file)

    # Pivot table to create a matrix
    matrix = cooccurrence_df.pivot(index='Keyword1', columns='Keyword2', values='Cooccurrence').fillna(0)

    # Plot heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(matrix, cmap="YlGnBu", linewidths=0.5)
    plt.title("Keyword Co-Occurrence Heatmap", fontsize=16)
    plt.xlabel("Keyword")
    plt.ylabel("Keyword")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Heatmap saved to {output_file}")

# File paths
cooccurrence_file = 'data/processed/cooccurrence_matrix.csv'
heatmap_output = 'data/visualizations/cooccurrence_heatmap.png'

# Generate heatmap
visualize_heatmap(cooccurrence_file, heatmap_output)
