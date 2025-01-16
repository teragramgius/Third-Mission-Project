import json
import re

def sanitize_json_file(input_file, sanitized_file):
    """
    Sanitize the raw JSON file to fix invalid escape sequences.

    Args:
        input_file (str): Path to the input JSON file.
        sanitized_file (str): Path to save the sanitized JSON file.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # Remove invalid escape sequences
    sanitized_content = re.sub(r'\\(?!["\\/bfnrtu])', r'', raw_content)

    with open(sanitized_file, 'w', encoding='utf-8') as f:
        f.write(sanitized_content)

    print(f"Sanitized JSON saved to {sanitized_file}")


def clean_content(input_file, output_file, debug_file):
    """
    Clean 'content' fields in the sanitized JSON file, ensuring all are strings.

    Args:
        input_file (str): Path to the sanitized JSON file.
        output_file (str): Path to save the cleaned JSON file.
        debug_file (str): Path to save problematic entries.

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
                    cleaned_data.append(item)
                elif isinstance(item['content'], list):
                    item['content'] = " ".join(map(str, item['content']))
                    cleaned_data.append(item)
                elif isinstance(item['content'], dict):
                    item['content'] = json.dumps(item['content'])
                    cleaned_data.append(item)
                elif item['content'] is None:
                    problematic_entries.append({
                        "index": idx,
                        "content": None,
                        "error": "Null content"
                    })
                else:
                    item['content'] = str(item['content'])
                    cleaned_data.append(item)
            else:
                problematic_entries.append({
                    "index": idx,
                    "content": None,
                    "error": "Missing 'content' field"
                })
        except Exception as e:
            problematic_entries.append({
                "index": idx,
                "content": item.get('content', None),
                "error": str(e)
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
    print(f"Cleaned content saved to {output_file}")

    if problematic_entries:
        with open(debug_file, 'w', encoding='utf-8') as f:
            json.dump(problematic_entries, f, ensure_ascii=False, indent=4)
        print(f"Problematic entries logged in {debug_file}")
    else:
        print("No problematic entries found.")

# File paths
raw_file = "data/processed/labeled_pages.json"
sanitized_file = "data/processed/labeled_pages_sanitized.json"
cleaned_file = "data/processed/cleaned_labeled_pages.json"
debug_file = "data/processed/problematic_entries.json"

# Step 1: Sanitize the JSON file
#sanitize_json_file(raw_file, sanitized_file)

# Step 2: Clean the sanitized JSON file
clean_content(sanitized_file, cleaned_file, debug_file)
