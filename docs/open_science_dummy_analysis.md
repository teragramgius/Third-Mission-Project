# Analysis and Usage of the Dummy Variable

## 1. Purpose of the Dummy Variable
The dummy variable `has_open_science_page` is a binary indicator that helps identify whether an Italian university has a webpage explicitly dedicated to open science. This variable plays a critical role in the project's exploratory and comparative analyses by adding a quantifiable measure of open science visibility at institutions.

### Benefits:
1. **Comparative Analysis:** Differentiate universities with visible open science initiatives from those without.
2. **Correlations:** Investigate relationships between having an open science page and network centrality, thematic focus, or other institutional characteristics.
3. **Policy Insights:** Assess how the presence of open science pages aligns with national or European open science policies.

## 2. Methods for Creating the Dummy Variable
### **Logic for Identification**
The dummy variable is created by checking if the university’s webpage URL contains specific keywords, visible in the data folder.
- **Value:**
  - `1` if the link contains any of these keywords.
  - `0` otherwise.

### **Implementation**
The preprocessing script `preprocess_data.py` includes a function to assign the dummy variable based on the URL:
```python
# Example function
keywords = ["open-science", "scienza-aperta", "openaccess", "ricerca-aperta"]
data['has_open_science_page'] = data['link'].apply(lambda x: int(any(keyword in x.lower() for keyword in keywords)))
```

## 3. Analysis of the Dummy Variable
### **Exploratory Data Analysis (EDA)**
1. **Frequency Analysis:**
   - Proportion of universities with and without open science pages.
2. **Geographical Trends:**
   - Are certain regions more likely to have open science pages?
3. **Thematic Comparison:**
   - Differences in the strategic narratives of universities with and without open science pages.

### **Network Analysis**
- **Node Attribute:** Use the dummy variable as a node attribute in the third mission network.
- **Centrality Comparisons:**
  - Compare centrality measures (e.g., PageRank, Eigenvector) between universities with and without open science pages.

### **Statistical Tests**
- Test hypotheses about the relationship between having an open science page and:
  - Centrality in the network.
  - Institutional characteristics (e.g., size, funding levels).
