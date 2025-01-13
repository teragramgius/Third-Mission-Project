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
