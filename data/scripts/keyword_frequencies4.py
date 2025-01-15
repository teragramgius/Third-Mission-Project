import json
from collections import Counter

def compute_keyword_frequencies(input_file, output_file):
    """
    Compute keyword frequencies from the refined keywords JSON file.

    Args:
        input_file (str): Path to the refined keywords JSON file.
        output_file (str): Path to save the keyword frequencies.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collect all keywords into a single list
    all_keywords = []
    for entry in data:
        if 'keywords' in entry:
            all_keywords.extend(entry['keywords'])

    # Count keyword occurrences
    keyword_counts = Counter(all_keywords)

    # Save keyword frequencies
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keyword_counts.most_common(), f, ensure_ascii=False, indent=4)

    print(f"Keyword frequencies saved to {output_file}")

# File paths
input_file = "data/processed/refined_keywords.json"  # Adjust to your actual file
output_file = "data/processed/updated_keyword_frequencies.json"

# Run the frequency computation
compute_keyword_frequencies(input_file, output_file)
