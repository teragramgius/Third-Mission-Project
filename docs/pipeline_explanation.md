# Third Mission Project: Updated Pipeline and References

## Overview

This document explains the updated pipeline of the Third Mission Project, focusing on analyzing open science narratives from Italian universities. It incorporates insights from relevant academic works and utilizes available open science taxonomies for enhanced validation and training.

---

## Pipeline Explanation

### **Step 1: Data Collection**

#### Objective

Collect primary and secondary webpage content related to open science from Italian university websites.

#### Process

1. **Scraping Main Pages**:
   - Fetched main open science pages using URLs collected from Italian universities.
   - Data saved in `data/raw/main_pages.json`.
2. **Parsing and Fetching Subpages**:
   - Extracted subpage links from main pages using `BeautifulSoup`.
   - Fetched subpage content and saved it in `data/raw/subpages.json`.
3. **Combining Datasets**:
   - Merged main and subpage datasets into a unified file, `data/raw/combined_open_science_pages.json`.

### **Step 2: Preprocessing**

#### Objective

Prepare the collected content for semantic validation and analysis.

#### Process

1. **HTML Cleaning**:
   - Cleaned raw HTML to remove tags, boilerplate text, and special characters.
   - Retained only plain text using the `preprocess_content.py` script.
   - Saved processed content to `data/processed/cleaned_pages.json`.

2. **Content Cleaning**:
   - Detected and removed malformed entries containing unreadable or non-printable characters.
   - Filtered entries with insufficient meaningful content (less than 10 characters).
   - Utilized the `clean_dataset.py` script to process `data/processed/labeled_pages.json` into a cleaned dataset saved as `data/processed/cleaned_labeled_pages.json`.
   
#### Results
- Entries with meaningful content were retained.
- Cleaned dataset is ready for semantic validation and tagging.

### **Step 3: Semantic Validation**

#### Objective

Ensure the relevance of the processed content to open science themes by comparing it to established open science concepts.

#### Process

1. **Reference Framework**:
   - Utilized open science taxonomies from authoritative online sources (e.g., OpenAIRE, UNESCO).
   - Reference texts define key themes and keywords, e.g.,:
     ```
     Open science promotes transparency, accessibility, and collaboration in research, emphasizing open access to publications and data.
     ```
2. **Semantic Similarity**:
   - Computed similarity scores between cleaned content and reference texts using a pre-trained embedding model (e.g., Sentence-BERT).
   - Retained pages with scores above a predefined threshold (e.g., 0.7).

### **Step 4: Content Analysis**

#### Objective

Extract insights about the framing of open science in university narratives.

#### Planned Methods

- **Keyword Extraction**:
  - Identify frequently used terms and concepts to understand the thematic focus.
- **Topic Modeling**:
  - Use Latent Dirichlet Allocation (LDA) or similar techniques to uncover dominant themes.
- **Word Embeddings**:
  - Analyze term relationships and clustering using word2vec or GloVe.

---

## References

1. **Nomoto et al. (2022)**: A survey on keyword extraction methodologies, providing insight into preprocessing and semantic analysis techniques.

   - *Reference*: Nomoto, Y., et al. (2022). *A survey of keyword extraction methodologies*. Springer.

2. **Lee and Chung (2023)**: A study on mapping open science research through bibliographic coupling, useful for understanding content relationships and focus areas.

   - *Reference*: Lee, H., & Chung, S. (2023). *Mapping open science research using a keyword bibliographic coupling analysis network*.

3. **Taxonomies and Frameworks**:

   - Leveraged authoritative sources such as OpenAIRE and UNESCO to define open science themes and validate the dataset.

4. **Inspiration**:

   - Workflow organization and clarity were inspired by a network analysis report on coronavirus research (unpublished). This report provided procedural guidance but was not directly cited.

---

## Next Steps

1. **Dataset Construction**:
   - Label existing content using open science taxonomies.
   - Build a training dataset for supervised or unsupervised learning tasks.
2. **NLP Analysis**:
   - Extract themes, keywords, and term relationships using the processed dataset.
3. **Validation and Insights**:
   - Compare findings against external open science datasets and frameworks.

This pipeline will continue evolving as the project progresses. Feedback and additional inputs are welcome.

