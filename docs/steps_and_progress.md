# Third Mission Project: Steps and Progress

## Overview
This document outlines the steps taken so far in the Third Mission Project, focusing on collecting, processing, and preparing data related to open science narratives from Italian universities. Each step is described in detail, including the rationale and methods used.

---

## 1. Data Collection

### **Objective**
Collect main and subpage content related to open science from Italian university websites.

### **Steps**
#### 1.1 Fetch Main Pages
- Used the `fetch_main_pages.py` script to scrape the primary open science pages listed in `data/raw/universities.json`.
- Saved the output to `data/raw/main_pages.json`.

#### 1.2 Parse and Fetch Subpages
- Extracted internal links from the main pages using `BeautifulSoup`.
- Fetched the content of these subpages using the `fetch_subpages.py` script.
- Saved the output to `data/raw/subpages.json`.

#### 1.3 Combine Main Pages and Subpages
- Merged the data from `main_pages.json` and `subpages.json` into a single dataset using `merge_datasets.py`.
- Saved the combined dataset to `data/raw/combined_open_science_pages.json`.

---

## 2. Preprocessing the Content

### **Objective**
Clean the raw HTML content from the combined dataset and prepare it for analysis.

### **Steps**
#### 2.1 HTML Cleaning
- Removed HTML tags and boilerplate text using `BeautifulSoup`.
- Retained only the plain text content for each page.

#### 2.2 Save Cleaned Data
- Used the `preprocess_content.py` script to process the combined dataset in `data/raw/combined_open_science_pages.json`.
- Saved the cleaned dataset to `data/processed/cleaned_pages.json`.

---

## 3. File and Directory Organization

### **Current Directory Structure**
```
Third-Mission-Project/
├── data/
│   ├── raw/               # Raw scraped content
│   │   ├── universities.json
│   │   ├── main_pages.json
│   │   ├── subpages.json
│   │   ├── combined_open_science_pages.json
│   ├── processed/         # Cleaned and preprocessed data
│   │   ├── cleaned_pages.json
├── scripts/               # Python scripts for data handling
│   ├── fetch_main_pages.py
│   ├── fetch_subpages.py
│   ├── preprocess_content.py
├── notebooks/             # Jupyter notebooks for analysis and visualization
├── results/               # Outputs of analysis and visualizations
├── README.md              # Project overview
```

---

## Summary
- **Data Collection**: Successfully scraped main and subpages, then combined them into a single dataset.
- **Preprocessing**: Cleaned the raw HTML content, producing a ready-to-analyze dataset.

Next steps involve:
1. **Semantic Validation**: Ensure the cleaned content is relevant to open science.
2. **NLP Analysis**: Extract insights such as keywords, topics, and narratives.

---

This document will be updated as the project progresses.

