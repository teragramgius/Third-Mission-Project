import json
import re

def clean_content(text):
    """
    Remove non-printable characters from text.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    return re.sub(r"[^\x20-\x7E]+", "", text)

def clean_dataset(input_file, output_file):
    """
    Clean the labeled dataset by removing malformed content and filtering invalid entries.

    Args:
        input_file (str): Path to the input JSON file with labeled pages.
        output_file (str): Path to save the cleaned dataset.

    Returns:
        None
    """
    # Load the dataset
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Clean and filter the dataset
    cleaned_data = []
    for item in data:
        if "content" in item:
            cleaned_text = clean_content(item["content"])
            if len(cleaned_text.strip()) > 10:  # Keep entries with meaningful content
                item["content"] = cleaned_text
                cleaned_data.append(item)

    # Save the cleaned dataset
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print(f"Cleaned dataset saved to {output_file}. Total entries: {len(cleaned_data)}")

# File paths
input_file = "data/processed/labeled_pages.json"
output_file = "data/processed/cleaned_labeled_pages.json"

# Clean the dataset
clean_dataset(input_file, output_file)
