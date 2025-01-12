# Third Mission Strategic Narratives - Network Analysis

## Purpose and Goals
This project explores the strategic narratives of Italian universities regarding their "third mission," with a specific focus on "open science" as a sub-topic. It combines network analysis and bibliometrics to identify influential papers, institutions, and thematic connections. 

## Subdirectories

1. **data:** Contains raw, processed, and visualization-ready datasets.
   - `raw/`: Initial collected data.
   - `processed/`: Preprocessed data ready for analysis.
   - `visualizations/`: Outputs of network visualizations.

2. **src:** Contains scripts for analysis, including:
   - `collect_data.py`: Scrapes or retrieves relevant datasets.
   - `preprocess_data.py`: Cleans and organizes the raw data.
   - `network_analysis.py`: Conducts network analysis and computes metrics.
   - `open_science_analysis.py`: Specialized analysis for "open science" narratives.

3. **notebooks:** Jupyter notebooks for exploratory data analysis and visualization.
   - `literature_review.ipynb`: Explores key papers and thematic trends.
   - `network_analysis.ipynb`: Interactive network analysis workflows.
   - `open_science_analysis.ipynb`: Sub-analysis for open science topics.

4. **docs:** Documentation files.
   - `project_overview.md`: General project description.
   - `choices_and_references.md`: Rationale for technical and thematic choices with citations.

5. **results:** Outputs and reports.
   - `visualizations/`: Network graphs and figures.
   - `open_science_reports/`: Reports specific to open science findings.
   - `third_mission_reports/`: Reports summarizing third mission findings.

6. **README.md:** High-level overview of the repository.

7. **LICENSE:** Licensing information for the repository.

8. **.gitignore:** Specifies files to be ignored by Git.

## Technical Stack
- **Data Collection:** `BeautifulSoup`, APIs (e.g., OpenAIRE, Semantic Scholar).
- **Analysis:** `NetworkX`, `pandas`, `matplotlib`.
- **Visualization:** Gephi, Plotly.

## How to Contribute
Contributions are welcome! Please open issues or submit pull requests for enhancements, bug fixes, or new features.
