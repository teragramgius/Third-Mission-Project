# Third Mission Project

## Overview
The Third Mission Project aims to explore how Italian universities articulate their strategic narratives regarding their "Third Mission," with a focus on **open science** as a key subtopic. By combining network analysis and text analysis methodologies, this project investigates how universities present their goals, values, and actions to promote open science and their broader societal engagement.

This repository includes:
- A dataset of Italian universities with information on their open science pages.
- A pipeline for longitudinal analysis using the Wayback Machine.
- Tools for extracting and analyzing strategic narratives.
- Scripts for preprocessing and analyzing collected data.

## Key Objectives
1. **Mapping Open Science Narratives**: Identify and analyze the strategic communication of open science across Italian universities.
2. **Longitudinal Analysis**: Track changes in strategic narratives over time using archived web data.
3. **Thematic Insights**: Extract keywords, themes, and sentiment to uncover shared and unique narratives.
4. **Comparative Analysis**: Explore regional and institutional differences in narratives and strategies.

## Progress
### Initial Setup
1. **Repository Structure**:
   - Organized into folders for data (`raw`, `processed`), scripts, notebooks, and results.
   - Key files include scraping pipelines, text preprocessing scripts, and analysis notebooks.

2. **Dataset**:
   - Compiled a dataset of Italian universities with URLs to their open science pages.
   - Included a dummy variable to indicate the presence of an open science page.

### Wayback Machine Integration
Inspired by the paper "The Internet Never Forgets: A Four-Step Scraping Tutorial, Codebase, and Database for Longitudinal Organizational Website Data" (Haans & Mertens, 2024), we developed a pipeline for longitudinal analysis:

1. **Fetching Archived Snapshots**:
   - Leveraged the Wayback Machine API to retrieve snapshots of university open science pages from 2015 to 2023.
   - Stored snapshot metadata (timestamp, archived URL) in `wayback_snapshots.json`.

2. **Parsing for Links to Subpages**:
   - Extracted internal links from archived pages to identify relevant subpages.
   - Filtered links based on keywords related to open science (e.g., "policy," "access," "events").

3. **Data Collection and Storage**:
   - Stored scraped data in the `data/raw` folder.
   - Planned structured preprocessing for thematic and sentiment analysis.

## Current Focus
### Tasks Completed:
1. **Dummy Variable Addition**:
   - Incorporated a dummy variable indicating whether a university has an open science page.

2. **Wayback Machine Pipeline**:
   - Developed a robust pipeline to fetch and save historical snapshots of open science pages.
   - Implemented error handling and logging for resilient scraping.

3. **Parsing Subpage Links**:
   - Enhanced the pipeline to extract and store links to relevant subpages for deeper analysis.

### Next Steps:
1. **Subpage Content Scraping**:
   - Scrape the content of parsed subpages to enrich the dataset.
   - Focus on extracting policy documents, event descriptions, and strategic goals.

2. **Text Analysis**:
   - Perform keyword extraction, topic modeling, and sentiment analysis on collected content.
   - Identify thematic trends and changes in narratives over time.

3. **Visualization**:
   - Create visualizations to compare narratives across institutions and time periods.

## Inspiration from Haans & Mertens (2024)
Key considerations adapted from the paper:
- **Temporal Depth**: Use longitudinal web data to capture how narratives evolve over time.
- **Subpage Analysis**: Parse links to uncover deeper insights into strategic communication.
- **Structured Framework**: Apply a four-step approach for data collection, preprocessing, and analysis.

## Repository Structure
```
Third-Mission-Project/
├── data/
│   ├── raw/         # Raw data (e.g., wayback snapshots, scraped content)
│   ├── processed/   # Cleaned and structured data
├── scripts/         # Python scripts for scraping and preprocessing
├── notebooks/       # Jupyter notebooks for analysis and visualization
├── results/         # Outputs (e.g., visualizations, summaries, models)
├── docs/            # Documentation files
├── README.md        # Project overview and instructions
```

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

Let me know if further refinements or additional details are needed!

