import json
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Initialize NLTK tools
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Preprocess text using tokenization and lemmatization.

    Args:
        text (str): Raw text to preprocess.

    Returns:
        str: Preprocessed text with lemmatized words.
    """
    tokens = word_tokenize(text.lower())
    return " ".join([lemmatizer.lemmatize(token) for token in tokens])

def fuzzy_match(keyword, content, threshold=80):
    """
    Perform fuzzy matching between a keyword and content.

    Args:
        keyword (str): Keyword to match.
        content (str): Text content to search.
        threshold (int): Minimum score for a match.

    Returns:
        bool: True if match exceeds threshold, False otherwise.
    """
    return fuzz.partial_ratio(keyword.lower(), content.lower()) >= threshold

def auto_tag_content(content, categories):
    """
    Tag content based on taxonomy keywords using preprocessing and fuzzy matching.

    Args:
        content (str): The text content to analyze.
        categories (dict): Dictionary of categories and their associated keywords.

    Returns:
        list: List of matching categories.
    """
    tags = []
    content_processed = preprocess_text(content)
    for category, keywords in categories.items():
        for keyword in keywords:
            keyword_processed = preprocess_text(keyword)
            if keyword_processed in content_processed or fuzzy_match(keyword, content_processed):
                print(f"Matched '{keyword}' in content for category '{category}'")  # Debug print
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

    # Load the taxonomy dictionary
    with open(taxonomy_file, "r", encoding="utf-8") as f:
        categories_keywords = json.load(f)

    # Debug: Print taxonomy structure
    print("Loaded Categories and Keywords:")
    print(json.dumps(categories_keywords, indent=4, ensure_ascii=False))

    # Apply tagging
    labeled_data = []
    for item in data:
        print(f"Processing URL: {item['url']}")
        tags = auto_tag_content(item["content"], categories_keywords)  # Use the dictionary here
        item["tags"] = tags
        labeled_data.append(item)
        print(f"Tags: {tags}")

    # Save the labeled dataset
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(labeled_data, f, ensure_ascii=False, indent=4)
    print(f"Labeled dataset saved to {output_file}")

# File paths
input_file = "data/processed/cleaned_pages.json"  # Path to your cleaned dataset
taxonomy_file = "data/raw/open_science_taxonomy.json"  # Path to your taxonomy dictionary
output_file = "data/processed/labeled_pages.json"  # Path to save the labeled dataset

# Label the dataset
label_dataset(input_file, taxonomy_file, output_file)
