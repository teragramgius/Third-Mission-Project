# Third Mission Project

## Overview
The Third Mission Project explores how Italian universities articulate their strategic narratives about their "Third Mission," with a focus on **open science** as a critical subdomain. Open science, encompassing open access and related practices, is seen as an integral part of the university's societal engagement and knowledge dissemination efforts.

This project draws inspiration from the methodology and framework outlined in the paper *The Internet Never Forgets: A Four-Step Scraping Tutorial, Codebase, and Database for Longitudinal Organizational Website Data* (Haans & Mertens, 2024). While the original intent was to perform a longitudinal analysis using the Wayback Machine, we currently focus on a contemporary analysis due to practical constraints and limited historical data availability.

## Key Objectives
1. **Mapping Open Science Narratives**:
   - Identify how universities frame open science as part of their third mission.
   - Explore whether open science pages emphasize topics like open access.

2. **Thematic Insights**:
   - Extract key themes, keywords, and concepts to understand the strategic focus.

3. **Semantic and Content Analysis**:
   - Assess the coherence and focus of the open science narratives.
   - Perform NLP-based analysis to uncover underlying patterns and narratives.

## Current Focus
### Contemporary Analysis
Given the current focus on contemporary narratives, our objectives are:
1. **Data Collection**:
   - Scrape open science pages and subpages from Italian university websites.
   - Organize content for semantic and thematic analysis.

2. **Semantic Validation**:
   - Ensure that collected pages are semantically coherent and relevant to open science.
   - Use clustering and similarity measures to refine the dataset.

3. **NLP-Based Content Analysis**:
   - Apply topic modeling, keyword extraction, and word embedding techniques.
   - Analyze how open science is framed, with particular attention to the emphasis on open access.

4. **Dataset Integration**:
   - Compare extracted insights with content from existing authoritative datasets, such as OpenAIRE or UNESCO materials.

## Repository Structure
```
Third-Mission-Project/
├── data/
│   ├── raw/         # Raw data (e.g., scraped content)
│   ├── processed/   # Cleaned and structured data
├── scripts/         # Python scripts for scraping and preprocessing
├── notebooks/       # Jupyter notebooks for analysis and visualization
├── results/         # Outputs (e.g., visualizations, summaries, models)
├── docs/            # Documentation files
├── README.md        # Project overview and instructions
```

## Next Steps
1. **Scraping Open Science Pages**:
   - Use the current dataset of Italian universities to scrape open science pages and subpages.
   - Store the content and metadata in `data/raw`.

2. **Perform Semantic Validation**:
   - Use NLP techniques to ensure relevance and coherence of the scraped pages.
   
3. **NLP Analysis**:
   - Conduct topic modeling and keyword extraction to uncover key narratives and themes.
   - Focus on identifying mentions and emphasis on open access within the broader open science framework.

4. **Document Findings**:
   - Summarize insights and highlight strategic narratives about open science.

## References
- Haans, R. F., & Mertens, F. (2024). *The Internet Never Forgets: A Four-Step Scraping Tutorial, Codebase, and Database for Longitudinal Organizational Website Data.*

# updates: Addressing Semantic Challenges in Open Science Webpages

## Overview
As we delved deeper into analyzing the strategic narratives of Italian universities regarding open science, we encountered a significant challenge: **the inconsistent semantic usage of university websites**. Many universities do not follow structured or keyword-rich approaches to their web design. Consequently, pages discussing open science are not always labeled or linked in ways that make them easily identifiable through automated methods.

This document outlines the problem, explores potential solutions, and defines the chosen approach to address this issue.

---

## Problem Statement
While parsing subpages from university websites, we noticed:
- **Inconsistent Keywords**: Many relevant pages lack the terms "open science" in their URLs or content.
- **Poor Semantic Structure**: Websites often have unstructured navigation or unrelated links embedded in key sections.
- **Missed Context**: Automated filtering based on keywords alone risks excluding pages with meaningful content.

These challenges limit the effectiveness of automated scraping and parsing, particularly when universities do not adhere to best practices in web design or semantic structuring.

---

## Potential Solutions
To address these limitations, we considered three approaches:

### 1. Manual Curation (Fetching by Hand)
**Description**: Manually navigate university websites to identify and collect pages relevant to open science.

**Pros**:
- High accuracy for identifying relevant content.
- Captures nuanced information missed by automated methods.

**Cons**:
- Time-intensive and laborious.
- Limited scalability for larger datasets or updates.

### 2. Enhanced Automated Methods (Chosen Approach)
**Description**: Use Natural Language Processing (NLP) to classify page content based on thematic relevance to open science, even when explicit keywords are missing.

**Steps**:
1. Parse all internal links from university pages.
2. Scrape the content of each linked page.
3. Use a pre-trained or custom-trained NLP model to classify content relevance.
4. Save the results for downstream analysis.

**Pros**:
- Scalable for large datasets.
- Reduces manual effort.
- Captures implicit relevance through content analysis.

**Cons**:
- Requires computational resources.
- Model accuracy depends on quality and relevance of training data.

### 3. Hybrid Approach
**Description**: Combine automated methods with manual validation.

**Pros**:
- Balances efficiency and accuracy.
- Allows refinement of automated methods through manual insights.

**Cons**:
- Still partially reliant on manual effort.
- May not be scalable for future updates.

---

## Chosen Approach: Enhanced Automated Methods
We opted for the **NLP-based automated approach** due to its scalability and ability to handle large datasets. This method aligns with our goal of creating a repeatable, extensible pipeline for analyzing strategic narratives over time.

---

## Training the NLP Model
To implement this approach, we will:

1. **Leverage Existing Datasets**:
   - Use publicly available datasets related to research, open science, or academic communication to train the NLP model.
   - Examples include datasets from OpenAIRE, CORE, or scholarly repositories like arXiv.

2. **Create a Training Pipeline**:
   - Preprocess and tokenize textual data.
   - Fine-tune a pre-trained language model (e.g., BERT, spaCy) on labeled data.

3. **Validate the Model**:
   - Evaluate performance using metrics like precision, recall, and F1 score.
   - Use manually curated data from selected universities to assess and refine the model.

4. **Integrate into the Pipeline**:
   - Parse subpages from archived snapshots or live websites.
   - Apply the NLP model to classify pages as relevant or not relevant to open science.

---

## Next Steps
1. **Develop Training Dataset**:
   - Identify and download datasets for initial training.
   - Manually label a small dataset of university subpages to use as validation data.

2. **Build the NLP Model**:
   - Use tools like Hugging Face Transformers or spaCy for model development.
   - Test the model on real university webpage data.

3. **Integrate and Test**:
   - Implement the NLP-based classifier into the existing Wayback Machine pipeline.
   - Run end-to-end tests on selected universities to validate performance.

4. **Document Findings**:
   - Summarize the results in terms of accuracy and scalability.
   - Highlight any limitations or areas for future improvement.

---

## Conclusion
This approach addresses the limitations of relying solely on keywords or manual curation. By incorporating advanced NLP techniques, we aim to build a robust system for identifying and analyzing open science narratives across Italian universities, regardless of their semantic inconsistencies.

---

