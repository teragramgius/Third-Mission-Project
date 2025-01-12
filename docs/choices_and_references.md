# Choices and References

## Technical Choices

### **1. Data Collection Tools**

- **Choice:** Use `BeautifulSoup` for web scraping and APIs like OpenAIRE for structured data retrieval.
- **Rationale:** These tools are effective for extracting structured and unstructured data from websites and APIs, ensuring comprehensive coverage of Italian universities' strategic documents.
- **References:**
  - OpenAIRE API documentation: [OpenAIRE](https://www.openaire.eu/)
  - Burton & Kebler (1960): Highlighting the value of comprehensive dataset collection.

### **2. Network Analysis Framework**

- **Choice:** Employ `NetworkX` for network modeling and analysis, supplemented by Gephi for visualization.
- **Rationale:** NetworkX is a robust library for constructing and analyzing complex networks. Gephi provides intuitive, high-quality visualizations.
- **References:**
  - Watts & Strogatz (1998): Discuss small-world networks and clustering.
  - Telesford et al. (2011): Framework for small-world network analysis.

### **3. Centrality Measures**

- **Choice:** Incorporate PageRank, Eigenvector centrality, and in-degree measures to identify influential nodes in the network.
- **Rationale:** These measures offer diverse perspectives on importance within a network, balancing utility and quality.
- **References:**
  - Page et al. (1999): Introduction of the PageRank algorithm.
  - Diallo et al. (2016): Comparison of centrality measures for identifying key papers.

### **4. Data Processing Tools**

- **Choice:** Use Python libraries (`pandas`, `numpy`) for cleaning and processing datasets.
- **Rationale:** These libraries are efficient for handling large datasets and preparing them for network analysis.
- **References:**
  - Nieminen et al. (2006): On the relationship between research quality and citation frequency.

## Thematic Choices

### **1. Focus on the Third Mission**

- **Choice:** Analyze Italian universities' narratives on societal impact, innovation, and public engagement.
- **Rationale:** The "third mission" reflects universities' broader societal roles, a crucial topic in higher education policy.
- **References:**
  - Martin & Irvine (1983): Discuss utility vs. quality in academic contributions.

### **2. Inclusion of Open Science**

- **Choice:** Treat open science as a critical sub-topic within the third mission.
- **Rationale:** Open science emphasizes transparency and collaboration, aligning with societal engagement goals.
- **References:**
  - Neylon & Wu (2009): On article-level metrics and scientific impact.

## Methodological Choices

### **1. Dataset Scope**

- **Choice:** Focus on Italian universities' documents and publications.
- **Rationale:** Restricting scope ensures relevance and manageability, while representing a national-level perspective.
- **References:**
  - Peroni (2020): On dataset preparation for context-specific analysis.

### **2. Weighted Networks**

- **Choice:** Incorporate journal importance as weights in the network.
- **Rationale:** Weighted networks provide a nuanced understanding of influence and connections.
- **References:**
  - Merton (1968): The Matthew Effect in science.
  - Price (1965): On cumulative advantage in citations.

### **3. Validation and Reliability**

- **Choice:** Validate measures through correlation with citation counts and other established metrics.
- **Rationale:** Ensures robustness and consistency of the workflow.
- **References:**
  - Burton & Kebler (1960): On the reliability of bibliometric measures.

## Future Directions

- Explore temporal trends in open science narratives.
- Develop workflows for integrating new data into the analysis.
- Compare findings across different national contexts.

