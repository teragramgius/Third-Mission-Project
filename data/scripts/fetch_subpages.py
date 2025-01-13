import requests
from bs4 import BeautifulSoup
import json
import os

def extract_subpage_links(html, base_url):
    """
    Extract internal links from a given HTML content.

    Args:
        html (str): The HTML content of the main page.
        base_url (str): The base URL of the main page.

    Returns:
        list: A list of unique subpage links.
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Filter for internal or relevant links
        if href.startswith('/'):  # Relative URL
            links.append(base_url + href)
        elif base_url in href:  # Absolute URL on the same domain
            links.append(href)
    return list(set(links))  # Remove duplicates

def fetch_subpages(main_pages):
    """
    Fetch subpages linked from main pages.

    Args:
        main_pages (list): List of dictionaries containing main page data.

    Returns:
        list: List of dictionaries with subpage data.
    """
    subpages = []
    for page in main_pages:
        base_url = page['url']
        print(f"Extracting subpage links from: {base_url}...")
        try:
            subpage_links = extract_subpage_links(page['content'], base_url=base_url)
            for link in subpage_links:
                print(f"Fetching subpage: {link}")
                try:
                    response = requests.get(link, timeout=10)
                    if response.status_code == 200:
                        print(f"Success: Fetched {link}")
                        subpages.append({
                            "university": page["university"],
                            "url": link,
                            "content": response.text,
                            "is_subpage": True
                        })
                    else:
                        print(f"Failed to fetch {link} (HTTP {response.status_code})")
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching {link}: {e}")
        except Exception as e:
            print(f"Error extracting links from {base_url}: {e}")
    return subpages

def save_subpages(subpages, output_file):
    """
    Save the subpages data to a JSON file.

    Args:
        subpages (list): List of subpage data dictionaries.
        output_file (str): Path to the output JSON file.

    Returns:
        None
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(subpages, f, ensure_ascii=False, indent=4)
    print(f"Saved subpages to {output_file}")

# Load main pages
with open("data/raw/main_pages.json", "r", encoding="utf-8") as f:
    main_pages = json.load(f)

# Fetch subpages
subpages = fetch_subpages(main_pages)

# Save subpages to file
save_subpages(subpages, "data/raw/subpages.json")
