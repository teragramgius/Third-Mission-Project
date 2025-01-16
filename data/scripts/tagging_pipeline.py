import json
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

# Initialize NLTK tools
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('italian'))

def preprocess_text(text):
    """
    Preprocess text using tokenization, lemmatization, and stopword removal.

    Args:
        text (str): Raw text to preprocess.

    Returns:
        str: Preprocessed text with lemmatized words.
    """
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stop_words and token.isalnum()]
    return " ".join(tokens)

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
            if keyword_processed in content_processed or fuzz.partial_ratio(keyword.lower(), content_processed) >= 80:
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

    # Apply tagging
    labeled_data = []
    for item in data:
        tags = auto_tag_content(item["content"], categories_keywords)
        item["tags"] = tags
        labeled_data.append(item)

    # Save the labeled dataset
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(labeled_data, f, ensure_ascii=False, indent=4)
    print(f"Labeled dataset saved to {output_file}")

# File paths
input_file = "data/processed/cleaned_pages.json"
taxonomy_file = "data/raw/open_science_taxonomy.json"
output_file = "data/processed/labeled_pages.json"

# Label the dataset
label_dataset(input_file, taxonomy_file, output_file)
