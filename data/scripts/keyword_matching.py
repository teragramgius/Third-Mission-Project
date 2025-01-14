import json

def load_taxonomy(json_file):
    """
    Load the open science taxonomy from a JSON file and return a dictionary of categories and keywords.

    Args:
        json_file (str): Path to the JSON taxonomy file.

    Returns:
        dict: A dictionary of categories and their associated keywords.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        taxonomy = json.load(f)
    keywords_dict = {}

    def extract_keywords(node, parent_category=""):
        """
        Recursively extract keywords from the taxonomy nodes.

        Args:
            node (dict): The current taxonomy node.
            parent_category (str): The parent category name.

        Returns:
            None (updates keywords_dict in place).
        """
        for category, content in node.items():
            if "keywords" in content:
                full_category = f"{parent_category} > {category}" if parent_category else category
                keywords_dict[full_category] = content["keywords"]
            if isinstance(content, dict):
                extract_keywords(content, f"{parent_category} > {category}" if parent_category else category)

    extract_keywords(taxonomy)
    return keywords_dict

def auto_tag_content(content, categories):
    """
    Tag content based on the presence of keywords for each category.

    Args:
        content (str): The text content to analyze.
        categories (dict): Dictionary of categories and their associated keywords.

    Returns:
        list: List of matching categories.
    """
    tags = []
    content_lower = content.lower()
    for category, keywords in categories.items():
        if any(keyword.lower() in content_lower for keyword in keywords):
            tags.append(category)
    return tags

def label_dataset(input_file, taxonomy_file, output_file):
    """
    Label the dataset using the taxonomy-based keyword matching.

    Args:
        input_file (str): Path to the input JSON file with cleaned content.
        taxonomy_file (str): Path to the JSON taxonomy file.
        output_file (str): Path to save the labeled dataset.

    Returns:
        None
    """
    # Load the cleaned dataset
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Load the taxonomy
    categories = load_taxonomy(taxonomy_file)

    # Apply tagging
    labeled_data = []
    for item in data:
        tags = auto_tag_content(item["content"], categories)
        item["tags"] = tags
        labeled_data.append(item)
        print(f"Labeled {item['url']} with tags: {tags}")

    # Save the labeled dataset
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(labeled_data, f, ensure_ascii=False, indent=4)
    print(f"Labeled dataset saved to {output_file}")

# File paths
input_file = "data/processed/cleaned_pages.json"
taxonomy_file = "data/raw/Open_Science_Taxonomy.json"
output_file = "data/processed/labeled_pages.json"

# Label the dataset
label_dataset(input_file, taxonomy_file, output_file)
