import json

def extract_keywords_from_taxonomy(json_file):
    """
    Extract categories and associated keywords from a taxonomy JSON file.

    Args:
        json_file (str): Path to the taxonomy JSON file.

    Returns:
        dict: A dictionary of categories and their associated keywords.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        taxonomy = json.load(f)

    keywords_dict = {}

    def parse_node(node, category_path=""):
        """
        Recursively parse the taxonomy JSON to extract categories and keywords.

        Args:
            node (dict): Current node in the taxonomy.
            category_path (str): Current category path.

        Returns:
            None: Updates the keywords_dict in place.
        """
        if isinstance(node, dict):
            for key, value in node.items():
                # Update category path
                new_category_path = f"{category_path} > {key}" if category_path else key

                # Check for keywords
                if "parole chiave" in value:
                    keywords_dict[new_category_path] = value["parole chiave"]

                # Recurse into sub-nodes
                parse_node(value, new_category_path)

    parse_node(taxonomy)
    return keywords_dict

# File path to the taxonomy JSON
taxonomy_file = "data/raw/open_science_taxonomy.json"

# Extract categories and keywords
categories_keywords = extract_keywords_from_taxonomy(taxonomy_file)

# Print the resulting dictionary
print(json.dumps(categories_keywords, indent=4, ensure_ascii=False))
