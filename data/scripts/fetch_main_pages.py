import requests
import json
import os

def fetch_main_pages(universities):
    """
    Fetch the main open science pages for a list of universities and save them to data/raw/main_pages.json.

    Args:
        universities (list): List of dictionaries with university names and open science URLs.

    Returns:
        None
    """
    main_pages = []
    for uni in universities:
        url = uni.get('open_science_url')  # Safely get the URL
        if url:  # Check if the URL is valid and not None
            print(f"Fetching: {url} for {uni['name']}...")
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"Success: Fetched {url}")
                    main_pages.append({
                        "university": uni["name"],
                        "url": url,
                        "content": response.text,
                        "is_subpage": False
                    })
                else:
                    print(f"Failed to fetch {url} (HTTP {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {url}: {e}")
        else:
            print(f"Skipping: No open science URL for {uni['name']}")

    # Save the data to data/raw/main_pages.json
    os.makedirs("data/raw", exist_ok=True)  # Ensure the directory exists
    with open("data/raw/main_pages.json", "w", encoding="utf-8") as f:
        json.dump(main_pages, f, ensure_ascii=False, indent=4)
    print("Saved main pages to data/raw/main_pages.json")


# Load universities data from JSON file
with open("data/raw/universities.json", "r", encoding="utf-8") as f:
    universities = json.load(f)

# Call the fetch_main_pages function
fetch_main_pages(universities)
