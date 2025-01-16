import json

def clean_content_debug(input_file, output_file, debug_file):
    """
    Debug and clean 'content' fields in the JSON file, ensuring all are strings.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the cleaned JSON file.
        debug_file (str): Path to save the problematic entries.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_data = []
    problematic_entries = []

    for idx, item in enumerate(data):
        try:
            # Check if 'content' exists
            if 'content' in item:
                if isinstance(item['content'], str):
                    # Content is a valid string
                    cleaned_data.append(item)
                elif isinstance(item['content'], list):
                    # Convert list to string
                    item['content'] = " ".join(map(str, item['content']))
                    cleaned_data.append(item)
                elif isinstance(item['content'], dict):
                    # Convert dictionary to JSON string
                    item['content'] = json.dumps(item['content'])
                    cleaned_data.append(item)
                elif item['content'] is None:
                    # Skip null content
                    problematic_entries.append({
                        "index": idx,
                        "content": None,
                        "error": "Null content"
                    })
                else:
                    # Convert any other type to a string
                    item['content'] = str(item['content'])
                    cleaned_data.append(item)
            else:
                # Log missing 'content' field
                problematic_entries.append({
                    "index": idx,
                    "content": None,
                    "error": "Missing 'content' field"
                })

        except Exception as e:
            # Catch and log unexpected errors
            problematic_entries.append({
                "index": idx,
                "content": item.get('content', None),
                "error": str(e)
            })

    # Save cleaned data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
    print(f"Cleaned content saved to {output_file}")

    # Save problematic entries
    if problematic_entries:
        with open(debug_file, 'w', encoding='utf-8') as f:
            json.dump(problematic_entries, f, ensure_ascii=False, indent=4)
        print(f"Problematic entries logged in {debug_file}")
    else:
        print("No problematic entries found.")

# File paths
input_file = "data/processed/labeled_pages.json"
output_file = "data/processed/cleaned_labeled_pages.json"
debug_file = "data/processed/problematic_entries.json"

# Debug and clean content
clean_content_debug(input_file, output_file, debug_file)
