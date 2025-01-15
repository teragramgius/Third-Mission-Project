import json
from rake_nltk import Rake
import nltk

# Download required NLTK data
import json
from rake_nltk import Rake
import nltk

# Download required NLTK resources
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

# Initialize RAKE with NLTK stopwords
rake = Rake()


# Initialize RAKE with NLTK
rake = Rake()

def extract_keywords(content):
    """
    Extract keywords from the given text content using RAKE.

    Args:
        content (str): Text content to analyze.

    Returns:
        list: A list of extracted keywords, sorted by relevance.
    """
    rake.extract_keywords_from_text(content)
    return rake.get_ranked_phrases()

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
