import json

def merge_datasets(main_pages_file, subpages_file, output_file):
    """
    Merge main pages and subpages into a single dataset and save to a JSON file.

    Args:
        main_pages_file (str): Path to the main pages JSON file.
        subpages_file (str): Path to the subpages JSON file.
        output_file (str): Path to save the combined JSON file.

    Returns:
        None
    """
    # Load main pages
    with open(main_pages_file, "r", encoding="utf-8") as f:
        main_pages = json.load(f)

    # Load subpages
    with open(subpages_file, "r", encoding="utf-8") as f:
        subpages = json.load(f)

    # Combine the datasets
    combined_data = main_pages + subpages

    # Save the combined dataset to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)

    print(f"Saved combined dataset to {output_file}")

# File paths
main_pages_file = "data/raw/main_pages.json"
subpages_file = "data/raw/subpages.json"
output_file = "data/raw/combined_open_science_pages.json"

# Merge datasets
merge_datasets(main_pages_file, subpages_file, output_file)
