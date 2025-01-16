import json
from collections import Counter
from itertools import combinations
import pandas as pd

def build_cooccurrence_matrix(input_file, output_file):
    """
    Build a co-occurrence matrix from refined keywords.
    
    Args:
        input_file (str): Path to the refined keywords file.
        output_file (str): Path to save the co-occurrence matrix as a CSV.
    """
    # Load refined keywords
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract keyword lists
    all_keyword_sets = [set(entry['refined_tags']) for entry in data if 'refined_tags' in entry]

    # Count co-occurrences
    cooccurrence_counts = Counter()
    for keywords in all_keyword_sets:
        for pair in combinations(keywords, 2):
            cooccurrence_counts[tuple(sorted(pair))] += 1

    # Convert to DataFrame
    cooccurrence_df = pd.DataFrame(
        [(k[0], k[1], v) for k, v in cooccurrence_counts.items()],
        columns=['Keyword1', 'Keyword2', 'Cooccurrence']
    )

    # Save to CSV
    cooccurrence_df.to_csv(output_file, index=False)
    print(f"Co-occurrence matrix saved to {output_file}")

# File paths
input_file = 'data/processed/refined_keywords.json'
output_file = 'data/processed/cooccurrence_matrix.csv'

# Build co-occurrence matrix
build_cooccurrence_matrix(input_file, output_file)
