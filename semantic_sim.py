from sentence_transformers import SentenceTransformer, util
import json

# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(taxonomy):
    """
    Generate embeddings for taxonomy categories using Sentence-BERT.

    Args:
        taxonomy (dict): Dictionary of categories and keywords.

    Returns:
        dict: Dictionary of categories and their embeddings.
    """
    category_embeddings = {}
    for category in taxonomy.keys():
        category_embeddings[category] = model.encode(category, convert_to_tensor=True)
    return category_embeddings

def refine_tags_with_similarity(content, category_embeddings, threshold=0.7):
    """
    Refine tags for content using semantic similarity.

    Args:
        content (str): The text content to analyze.
        category_embeddings (dict): Dictionary of category embeddings.
        threshold (float): Similarity score threshold for tagging.

    Returns:
        list: List of refined categories.
    """
    content_embedding = model.encode(content, convert_to_tensor=True)
    refined_tags = []
    for category, embedding in category_embeddings.items():
        similarity = util.pytorch_cos_sim(content_embedding, embedding).item()
        if similarity >= threshold:
            refined_tags.append(category)
    return refined_tags

def refine_dataset(input_file, taxonomy_file, output_file, threshold=0.7):
    """
    Refine dataset tags using semantic similarity.

    Args:
        input_file (str): Path to the input JSON file with labeled content.
        taxonomy_file (str): Path to the JSON taxonomy file.
        output_file (str): Path to save the refined dataset.
        threshold (float): Similarity score threshold for tagging.

    Returns:
        None
    """
    # Load the labeled dataset
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Load the taxonomy dictionary
    with open(taxonomy_file, "r", encoding="utf-8") as f:
        categories_keywords = json.load(f)

    # Generate category embeddings
    category_embeddings = generate_embeddings(categories_keywords)

    # Refine tags
    refined_data = []
    for item in data:
        print(f"Processing URL: {item['url']}")
        refined_tags = refine_tags_with_similarity(item["content"], category_embeddings, threshold)
        item["refined_tags"] = refined_tags
        refined_data.append(item)
        print(f"Refined Tags: {refined_tags}")

    # Save the refined dataset
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(refined_data, f, ensure_ascii=False, indent=4)
    print(f"Refined dataset saved to {output_file}")

# File paths
input_file = "data/processed/labeled_pages.json"  # Path to your labeled dataset
taxonomy_file = "data/raw/open_science_taxonomy.json"  # Path to your taxonomy dictionary
output_file = "data/processed/refined_pages.json"  # Path to save the refined dataset

# Refine dataset
refine_dataset(input_file, taxonomy_file, output_file)
