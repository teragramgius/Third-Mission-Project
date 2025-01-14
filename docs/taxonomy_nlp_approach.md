# Documentation: Taxonomy and NLP Approaches in the Pipeline

## Overview
This document explains the rationale behind the chosen approach to integrating taxonomy-based and NLP-based techniques in the pipeline for analyzing open science narratives. It highlights the options considered, their advantages, and why a particular method was selected for this project.

---

## Options Considered

### **Option 1: Taxonomy First, NLP Second**
1. **Process**:
   - Use taxonomy-based keyword matching to tag content initially.
   - Refine the labeled data using NLP techniques, such as semantic similarity or supervised learning.

2. **Advantages**:
   - Straightforward and interpretable.
   - The taxonomy provides a clear structure and categories, ensuring alignment with established concepts in open science.
   - Advanced NLP methods build on an already structured dataset, enabling better supervised learning and insights.

3. **Disadvantages**:
   - May miss themes not explicitly defined in the taxonomy.

4. **Use Case**:
   - Best when the taxonomy is comprehensive and well-defined, as is the case with the Open Science taxonomy provided.

---

### **Option 2: NLP First, Taxonomy Validation**
1. **Process**:
   - Use unsupervised NLP techniques (e.g., topic modeling) to discover topics or themes in the data.
   - Validate and refine these topics using the taxonomy to align them with predefined categories.

2. **Advantages**:
   - Allows for discovering emerging themes or patterns beyond the taxonomy.
   - Identifies potential gaps or overlaps in the taxonomy.

3. **Disadvantages**:
   - Requires manual alignment between NLP-generated topics and taxonomy categories.
   - Less structured compared to taxonomy-first approaches.

4. **Use Case**:
   - Suitable when the taxonomy might be incomplete or when exploratory analysis is needed.

---

### **Option 3: Parallel Taxonomy and NLP**
1. **Process**:
   - Simultaneously apply taxonomy-based tagging and NLP-based semantic similarity or topic modeling.
   - Compare and combine results from both approaches.

2. **Advantages**:
   - Combines the strengths of taxonomy and NLP techniques.
   - Enables both structure and nuance in tagging and analysis.

3. **Disadvantages**:
   - More complex to implement and interpret.
   - Requires significant computational resources for NLP tasks.

4. **Use Case**:
   - Ideal for large datasets where taxonomy and NLP can complement each other.

---

## Chosen Approach: Taxonomy First, NLP Second

### **Why This Approach?**
1. **Comprehensive Taxonomy**:
   - The Open Science taxonomy provided is detailed and authoritative, covering key categories such as open access, open data, and open reproducible research.
   - It serves as a robust foundation for initial tagging and analysis.

2. **Simplicity and Interpretability**:
   - Taxonomy-based keyword matching is easy to implement and provides clear, interpretable results.
   - By starting with a structured dataset, subsequent NLP techniques can focus on refinement and additional insights.

3. **Complementary NLP Techniques**:
   - Semantic similarity (e.g., Sentence-BERT) will refine and validate the taxonomy-based tags, ensuring nuanced alignment with the taxonomy themes.
   - Topic modeling will help uncover patterns or themes not explicitly defined in the taxonomy, offering exploratory insights.

### **Implementation Steps**
1. **Taxonomy-Based Tagging**:
   - Use the provided taxonomy to tag content based on predefined keywords.
   - Save the labeled dataset for further refinement.

2. **NLP Refinement**:
   - Apply semantic similarity to refine taxonomy-based tags.
   - Use topic modeling to explore additional patterns and validate taxonomy coverage.

---

## Process: Taxonomy-Based Tagging

### **1. Initial Setup**
- The taxonomy was provided as a JSON file (`Open_Science_Taxonomy.json`), containing categories and associated keywords.
- A cleaned dataset of webpage content (`cleaned_pages.json`) was prepared in a previous step.

### **2. Transforming Taxonomy**
- The taxonomy JSON file was parsed into a Python dictionary (`categories_keywords`) containing categories and their keywords.

Example:
```json
{
    "Open Science > Open Access": [
        "open access",
        "OA",
        "free publications"
    ],
    "Open Science > Open Data": [
        "data sharing",
        "open datasets"
    ]
}
```

This step ensures the taxonomy is structured for efficient keyword matching.

### **3. Matching Logic**
The following enhancements were added to ensure robust tagging:

1. **Keyword Preprocessing**:
   - Text preprocessing (lowercasing, tokenization, and lemmatization) ensures that variations like "publishing" and "publish" match correctly.

2. **Fuzzy Matching**:
   - Approximate matches (e.g., "open-acess" vs. "open access") were handled using fuzzy matching with a configurable threshold.

3. **Combination**:
   - Both exact and fuzzy matching were applied for each keyword in the taxonomy.

### **4. Tagging Pipeline**
- The `auto_tag_content` function applies the taxonomy to each content item in the dataset, generating tags for matching categories.
- Example:

```python
sample_content = "Open science supports open access to research publications and data."
tags = auto_tag_content(sample_content, categories_keywords)
print(f"Tags: {tags}")
```

### **5. Output**
- The tagged dataset is saved as `labeled_pages.json`, containing the original content and the matched tags.
- Example:

```json
[
    {
        "university": "Università degli Studi dell'Aquila",
        "url": "https://www.univaq.it/section.php?id=2265",
        "content": "Open science promotes transparency and accessibility in research...",
        "tags": [
            "Open Science > Open Access",
            "Open Science > Open Data"
        ]
    }
]
```

---

## Next Steps
1. **Validate Tags**:
   - Manually review samples to ensure tags are accurate and meaningful.
2. **Refine Taxonomy**:
   - Expand keywords or adjust fuzzy matching thresholds as needed.
3. **Proceed to NLP Refinement**:
   - Use Sentence-BERT or topic modeling for further analysis.

