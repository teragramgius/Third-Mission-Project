import json
from rake_nltk import Rake
import nltk
from nltk.corpus import stopwords

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load Italian stopwords
stop_words = set(stopwords.words('italian'))

# Initialize RAKE with NLTK stopwords
rake = Rake(stopwords=stop_words)

def extract_keywords(content):
    """
    Extract keywords from the given text content using RAKE.

    Args:
        content (str): Text content to analyze.

    Returns:
        list: A list of extracted keywords, sorted by relevance.
    """
    rake.extract_keywords_from_text(content)
    keywords = rake.get_ranked_phrases()
    # Filter out short words and irrelevant phrases
    keywords = [kw for kw in keywords if len(kw.split()) > 1 and not any(word in stop_words for word in kw.split())]
    return keywords

def process_content(input_file, output_file):
    """
    Process the validated content to extract keywords and save results.

    Args:
        input_file (str): Path to the input JSON file with validated content.
        output_file (str): Path to save the extracted keywords.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    processed_data = []

    for item in data:
        if 'content' in item and item['content'].strip():
            keywords = extract_keywords(item['content'])
            processed_data.append({
                'url': item.get('url'),
                'content': item['content'],
                'keywords': keywords
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)

    print(f"Keywords extracted and saved to {output_file}")

# File paths
input_file = "data/processed/cleaned_labeled_pages.json"
output_file = "data/processed/keywords.json"

# Extract keywords from validated content
process_content(input_file, output_file)
