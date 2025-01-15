import json
import re

def clean_text(text):
    """
    Clean a text string by removing unwanted characters, normalizing spaces,
    and converting to lowercase.

    Args:
        text (str): The input text to clean.

    Returns:
        str: The cleaned text.
    """
    # Remove non-alphanumeric characters except spaces
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    # Convert to lowercase
    return text.lower()

def clean_keywords_file(input_file, output_file):
    """
    Clean the contents of a keywords JSON file.

    Args:
        input_file (str): Path to the input JSON file with raw keywords.
        output_file (str): Path to save the cleaned JSON file.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_data = []
    for entry in data:
        # Clean content if it exists
        if 'keywords' in entry and isinstance(entry['keywords'], list):
            cleaned_keywords = [clean_text(keyword) for keyword in entry['keywords'] if keyword.strip()]
            entry['keywords'] = [kw for kw in cleaned_keywords if len(kw) > 2]  # Keep keywords longer than 2 chars
            cleaned_data.append(entry)

    # Save the cleaned data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print(f"Cleaned keywords saved to {output_file}")

# File paths
input_file = "data/processed/keywords.json"  # Replace with your actual file path
output_file = "data/processed/cleaned_keywords.json"

# Run the cleaning process
clean_keywords_file(input_file, output_file)
