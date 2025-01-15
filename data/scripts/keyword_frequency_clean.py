import json
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_keyword(keyword):
    """
    Cleans a single keyword by removing non-alphabetic characters and short/empty strings.
    """
    keyword = re.sub(r'[^a-zA-Z ]', '', keyword).strip()  # Keep only letters
    if len(keyword) >= 3 and keyword.lower() not in stop_words:  # Filter short words and stopwords
        return keyword.lower()
    return None

def clean_keywords(keywords):
    """
    Cleans a list of keywords by applying the clean_keyword function to each.
    """
    return [kw for kw in (clean_keyword(kw) for kw in keywords) if kw]

def clean_and_analyze_keywords(input_file, output_file):
    """
    Cleans and analyzes keyword frequencies from the extracted keywords JSON file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_keywords = []
    for item in data:
        if 'keywords' in item:
            cleaned = clean_keywords(item['keywords'])
            all_keywords.extend(cleaned)

    # Count keyword occurrences
    keyword_counts = Counter(all_keywords)

    # Save cleaned and counted keywords
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keyword_counts.most_common(), f, ensure_ascii=False, indent=4)

    print(f"Cleaned keyword frequencies saved to {output_file}")

# File paths
input_file = "data/processed/keywords.json"
output_file = "data/processed/cleaned_keyword_frequencies.json"

# Run cleaning and analysis
clean_and_analyze_keywords(input_file, output_file)
