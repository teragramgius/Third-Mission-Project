from bs4 import BeautifulSoup
import json

def clean_html_content(content):
    """
    Remove HTML tags and clean text content.

    Args:
        content (str): Raw HTML content.

    Returns:
        str: Cleaned plain text.
    """
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator=" ")  # Extract plain text with spaces between elements
    return " ".join(text.split())  # Remove extra whitespace

def preprocess_content(input_file, output_file):
    """
    Preprocess raw HTML content from a JSON file and save the cleaned data.

    Args:
        input_file (str): Path to the input JSON file with raw HTML content.
        output_file (str): Path to save the cleaned JSON file.

    Returns:
        None
    """
    # Load combined data
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Preprocess content
    cleaned_data = []
    for item in data:
        cleaned_text = clean_html_content(item["content"])
        cleaned_data.append({
            "university": item["university"],
            "url": item["url"],
            "content": cleaned_text,
            "is_subpage": item["is_subpage"]
        })

    # Save cleaned data
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print(f"Saved cleaned content to {output_file}")

# File paths
input_file = "data/raw/combined_open_science_pages.json"
output_file = "data/processed/cleaned_pages.json"

# Preprocess content
preprocess_content(input_file, output_file)
