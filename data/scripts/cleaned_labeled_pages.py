import json

def clean_content_debug(input_file, output_file):
    """
    Debug and clean 'content' fields in the JSON file, ensuring all are strings.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the cleaned JSON file.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_data = []
    problematic_entries = []

    for idx, item in enumerate(data):
        # Check if 'content' exists
        if 'content' in item:
            if isinstance(item['content'], str):
                cleaned_data.append(item)  # Valid string
            else:
                try:
                    # Attempt to convert to string
                    item['content'] = str(item['content'])
                    cleaned_data.append(item)
                except Exception as e:
                    # Log problematic entry with index and error
                    problematic_entries.append({
                        "index": idx,
                        "content": item['content'],
                        "error": str(e)
                    })
        else:
            # Log items missing 'content' field
            problematic_entries.append({
                "index": idx,
                "content": None,
                "error": "Missing 'content' field"
            })

    # Save cleaned data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
    print(f"Cleaned content saved to {output_file}")

    # Save problematic entries for review
    if problematic_entries:
        with open("problematic_entries.json", 'w', encoding='utf-8') as f:
            json.dump(problematic_entries, f, ensure_ascii=False, indent=4)
        print("Problematic entries logged in 'problematic_entries.json'")

# File paths
input_file = "data/processed/labeled_pages.json"
output_file = "data/processed/cleaned_labeled_pages.json"

# Debug and clean content
clean_content_debug(input_file, output_file)
