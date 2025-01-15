# Third Mission Project: Steps and Progress

## Overview
This document outlines the steps taken so far in the Third Mission Project, focusing on collecting, processing, and analyzing data related to open science narratives from Italian universities. Each step is described in detail, including the rationale and methods used.

---

## 1. Data Collection

### Objective
Collect main and subpage content related to open science from Italian university websites.

### Steps
#### **1.1 Fetch Main Pages**
- **Method**: Used the `fetch_main_pages.py` script to scrape the primary open science pages listed in `data/raw/universities.json`.
- **Output**: Data saved to `data/raw/main_pages.json`.

#### **1.2 Parse and Fetch Subpages**
- **Method**: Extracted internal links from the main pages using `BeautifulSoup`. Fetched the content of these subpages using the `fetch_subpages.py` script.
- **Output**: Data saved to `data/raw/subpages.json`.

#### **1.3 Combine Main Pages and Subpages**
- **Method**: Merged the data from `main_pages.json` and `subpages.json` into a single dataset using `merge_datasets.py`.
- **Output**: Combined dataset saved to `data/raw/combined_open_science_pages.json`.

---

## 2. Preprocessing the Content

### Objective
Clean the raw HTML content from the combined dataset and prepare it for analysis.

### Steps
#### **2.1 HTML Cleaning**
- **Method**: Removed HTML tags, boilerplate text, and special characters using `BeautifulSoup`.
- **Output**: Cleaned text retained for each page.

#### **2.2 Save Cleaned Data**
- **Method**: Used the `preprocess_content.py` script to process the combined dataset in `data/raw/combined_open_science_pages.json`.
- **Output**: Cleaned dataset saved to `data/processed/cleaned_pages.json`.

---

## 3. Semantic Validation

### Objective
Ensure the cleaned content is relevant to open science themes.

### Steps
#### **3.1 Define Taxonomy**
- **Method**: Built a taxonomy of open science terms using authoritative sources such as OpenAIRE and UNESCO.
- **Output**: Saved taxonomy as `data/taxonomy.json`.

#### **3.2 Tag Content**
- **Method**: Used the taxonomy to label pages with relevant open science tags. Implemented keyword matching with fuzzy logic to account for variations in terms.
- **Output**: Labeled dataset saved to `data/processed/labeled_pages.json`.

#### **3.3 Refine Tags**
- **Method**: Applied additional refinement by:
  - Removing irrelevant terms and duplicate entries.
  - Introducing fuzzy matching and a threshold-based relevance system.
- **Output**: Refined dataset saved to `data/processed/refined_keywords.json`.

---

## 4. Keyword Analysis and Visualization

### Objective
Identify and visualize frequently occurring terms to understand thematic focus.

### Steps
#### **4.1 Keyword Extraction**
- **Method**: Extracted keywords using domain-specific stop words and cleaned irrelevant terms (e.g., Italian stop words).
- **Output**: Cleaned keyword frequencies saved to `data/processed/keyword_frequencies.json`.

#### **4.2 Frequency Visualization**
- **Method**: Visualized keyword frequencies through:
  - A **word cloud** to show the most frequent terms.
  - A **bar chart** for the top 20 keywords.
- **Output**:
  - Word cloud: `data/visualizations/refined_wordcloud_debug.png`
  - Bar chart: `data/visualizations/refined_barchart_debug.png`.

---

## 5. File and Directory Organization

### Current Directory Structure
```plaintext
Third-Mission-Project/
├── data/
│   ├── raw/               # Raw scraped content
│   │   ├── universities.json
│   │   ├── main_pages.json
│   │   ├── subpages.json
│   │   ├── combined_open_science_pages.json
│   ├── processed/         # Cleaned and processed data
│   │   ├── cleaned_pages.json
│   │   ├── labeled_pages.json
│   │   ├── refined_keywords.json
│   │   ├── keyword_frequencies.json
├── scripts/               # Python scripts for data handling
│   ├── fetch_main_pages.py
│   ├── fetch_subpages.py
│   ├── preprocess_content.py
│   ├── refine_keywords.py
│   ├── visualize_refined_keywords.py
├── notebooks/             # Jupyter notebooks for analysis and visualization
├── results/               # Outputs of analysis and visualizations
├── README.md              # Project overview
