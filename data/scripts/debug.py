# 1. Check Content Quality
'''
import json

with open("data/processed/labeled_pages.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data[:5]:  # Check the first 5 entries
    print(f"URL: {item['url']}")
    print(f"Content: {item['content'][:300]}")  # Print the first 300 characters
    print("-" * 50)
'''

# 2. Test Taxonomy Categories
'''
import json

with open("data/raw/open_science_taxonomy.json", "r", encoding="utf-8") as f:
    categories_keywords = json.load(f)

for category in categories_keywords.keys():
    print(f"Category: {category}")



#3. Test a Single Content Snippet
sample_content = "Open science ensures free access to research publications and encourages transparency."
sample_taxonomy = {
    "Open Science > Open Access": ["open access", "OA", "free access"],
    "Open Science > Open Data": ["data sharing", "datasets", "open data"]
}

# Generate embeddings for taxonomy
category_embeddings = generate_embeddings(sample_taxonomy)

# Test similarity
tags = refine_tags_with_similarity(sample_content, category_embeddings, threshold=0.3)
print(f"Content: {sample_content}")
print(f"Tags: {tags}")

'''
