import json
from collections import Counter
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

# Download necessary resources
nltk.download("stopwords")

# Custom and Italian stop words
italian_stop_words = set(stopwords.words("italian"))
custom_stop_words = {"cookies", "terms", "privacy", "page", "image", "javascript", "button", "com", "iva", 
                     "università", "scienza", "pubblico", "ricerca"}

# Initialize Italian stemmer
stemmer = SnowballStemmer("italian")

def flatten_taxonomy(taxonomy_data):
    """
    Flatten a taxonomy structure into a set of unique keywords.
    """
    flattened = set()
    if isinstance(taxonomy_data, list):
        for term in taxonomy_data:
            if isinstance(term, str):
                flattened.add(term)
    elif isinstance(taxonomy_data, dict):
        for key, values in taxonomy_data.items():
            if isinstance(values, list):
                for term in values:
                    if isinstance(term, str):
                        flattened.add(term)
    return flattened

def clean_and_filter_keywords(keyword_list):
    """
    Clean and filter keywords by removing stop words, splitting long phrases, and stemming.
    """
    processed_keywords = []
    for kw in keyword_list:
        words = kw.split()
        for word in words:
            word = word.lower()  # Lowercase
            word = re.sub(r'[^a-zA-Z0-9]', '', word)  # Remove non-alphanumeric
            if len(word) > 2 and word not in italian_stop_words and word not in custom_stop_words:
                stemmed_word = stemmer.stem(word)
                processed_keywords.append(stemmed_word)
    return processed_keywords

def visualize_keyword_frequencies(input_file, taxonomy_file, output_wordcloud, output_barchart, top_n=20):
    """
    Visualize keyword frequencies using a word cloud and a bar chart.
    """
    # Load keyword frequencies
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load taxonomy
    with open(taxonomy_file, 'r', encoding='utf-8') as f:
        taxonomy_data = json.load(f)
    taxonomy_terms = flatten_taxonomy(taxonomy_data)

    # Collect and filter all keywords
    all_keywords = []
    for entry in data:
        if 'keywords' in entry:
            all_keywords.extend(clean_and_filter_keywords(entry['keywords']))

    # Debug: Check keywords before filtering
    print("Total keywords before filtering:", len(all_keywords))
    print("Cleaned keywords (sample):", all_keywords[:10])

    # Count keyword occurrences
    keyword_counts = Counter(all_keywords)

    # Apply minimum frequency threshold with relaxed filtering
    filtered_keyword_counts = {
        kw: freq for kw, freq in keyword_counts.items()
        if freq > 2 and (kw in taxonomy_terms or len(kw) > 2)
    }

    # Debug: Check filtered results
    print("Filtered keywords (sample):", list(filtered_keyword_counts.items())[:10])

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(filtered_keyword_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Refined Keyword Frequencies Word Cloud")
    plt.savefig(output_wordcloud)
    print(f"Word cloud saved to {output_wordcloud}")
    plt.close()

    # Bar chart for top N keywords
    top_keywords = sorted(filtered_keyword_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    keywords, frequencies = zip(*top_keywords) if top_keywords else ([], [])

    plt.figure(figsize=(10, 6))
    plt.bar(keywords, frequencies)
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.title(f"Top {top_n} Keywords")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_barchart)
    print(f"Bar chart saved to {output_barchart}")
    plt.close()

# File paths
input_file = "data/processed/refined_keywords.json"
taxonomy_file = "data/raw/open_science_taxonomy.json"
output_wordcloud = "data/visualizations/refined_wordcloud_debug.png"
output_barchart = "data/visualizations/refined_barchart_debug.png"

# Generate visualizations
visualize_keyword_frequencies(input_file, taxonomy_file, output_wordcloud, output_barchart)
