import json
import re
from rapidfuzz import fuzz  # Replace with fuzzywuzzy if necessary


def flatten_taxonomy(taxonomy_data):
    """
    Flatten a taxonomy structure into a set of unique keywords.

    Args:
        taxonomy_data (dict or list): Taxonomy data, either as a list of terms or a nested dictionary.

    Returns:
        set: A set of flattened keywords.
    """
    flattened = set()
    if isinstance(taxonomy_data, list):
        # Handle flat list of terms
        for term in taxonomy_data:
            if isinstance(term, str):
                flattened.add(term)
    elif isinstance(taxonomy_data, dict):
        # Handle nested dictionary structure
        for key, values in taxonomy_data.items():
            if isinstance(values, list):
                for term in values:
                    if isinstance(term, str):
                        flattened.add(term)
    return flattened


def is_relevant_keyword(keyword, taxonomy):
    """
    Check if a keyword is relevant based on the taxonomy.

    Args:
        keyword (str): Keyword to validate.
        taxonomy (set): Set of valid taxonomy terms.

    Returns:
        bool: True if the keyword is relevant, False otherwise.
    """
    return any(fuzz.partial_ratio(keyword, term) > 80 for term in taxonomy)


def split_long_keywords(keyword):
    """
    Split long keywords into shorter phrases if applicable.

    Args:
        keyword (str): The keyword to split.

    Returns:
        list: List of shorter keywords.
    """
    return [kw.strip() for kw in re.split(r'[,;:]', keyword) if len(kw.strip()) > 2]


def refine_keywords(input_file, output_file, taxonomy_file):
    """
    Refine keywords by removing duplicates, irrelevant terms, and noise.

    Args:
        input_file (str): Path to the cleaned keywords JSON file.
        output_file (str): Path to save the refined keywords.
        taxonomy_file (str): Path to the taxonomy JSON file.

    Returns:
        None
    """
    # Load cleaned keywords
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load taxonomy
    with open(taxonomy_file, 'r', encoding='utf-8') as f:
        taxonomy_data = json.load(f)

    # Flatten taxonomy into a set
    taxonomy = flatten_taxonomy(taxonomy_data)

    refined_data = []
    for entry in data:
        if 'keywords' in entry:
            cleaned_keywords = set()
            for keyword in entry['keywords']:
                # Split long keywords and check relevance
                for sub_keyword in split_long_keywords(keyword):
                    if is_relevant_keyword(sub_keyword, taxonomy):
                        cleaned_keywords.add(sub_keyword.lower())

            entry['keywords'] = list(cleaned_keywords)
            refined_data.append(entry)

    # Save refined data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(refined_data, f, ensure_ascii=False, indent=4)

    print(f"Refined keywords saved to {output_file}")


# File paths
input_file = "data/processed/cleaned_keywords.json"  # Adjust path as needed
output_file = "data/processed/refined_keywords.json"
taxonomy_file = "data/raw/open_science_taxonomy.json"  # Path to your taxonomy JSON

# Run refinement process
refine_keywords(input_file, output_file, taxonomy_file)
