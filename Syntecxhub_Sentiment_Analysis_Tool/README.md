# Task 2: Sentiment Analysis Tool

<p align="center">
  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-NLP-success)
![Project](https://img.shields.io/badge/Project-Sentiment%20Analysis-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

</p>

<p align="center">
  An end-to-end <strong>Machine Learning NLP pipeline</strong> for sentiment classification.<br>
  Train, evaluate, persist, and interactively test sentiment prediction models directly from the command line.
</p>

---

## Project Overview

This project automates sentiment classification by categorizing text into binary sentiment classes:

- **Positive**
- **Negative**

The application features a complete machine learning workflow, including:

- Dataset generation and ingestion
- NLP preprocessing and token cleaning
- Text vectorization
- Model training and evaluation
- Model persistence
- Interactive command-line inference

The system supports both internally generated datasets containing **400+ balanced samples** and externally supplied CSV datasets.

Developed as **Project 2** during my **Artificial Intelligence Internship** at **Syntecxhub**.

---

##  Core Features

-  **Custom NLP Preprocessing**  
  Cleans text using Regular Expressions (RegEx) by removing URLs, user mentions, hashtags, special characters, and enforcing token-length constraints.

-  **Stop-Word Filtering**  
  Uses an in-memory stop-word set to eliminate non-informative grammatical words.

-  **Dual Vectorization Engines**  
  Supports both:
  - **TF-IDF Vectorizer**
  - **Count Vectorizer**

  Includes configurable **N-Gram ranges (`1, 2`)**.

-  **Alternative Classification Models**  
  Dynamically trains either:
  - **Logistic Regression**
  - **Multinomial Naive Bayes**

-  **Comprehensive Evaluation Metrics**  
  Generates:
  - Accuracy Score
  - F1 Score
  - Precision
  - Recall
  - Full Classification Report

-  **Model Persistence**  
  Saves trained models, vectorizers, and metadata using `joblib` for future reuse.

-  **Interactive Analysis CLI**  
  Provides a real-time command-line interface for sentiment prediction and confidence inspection.

---

## Tech Stack & Dependencies

| Library / Tool | Purpose |
|----------------|---------|
| **Python 3** | Core development language |
| **scikit-learn** | Feature extraction, model training, evaluation, and dataset splitting |
| **pandas** | Dataset manipulation and CSV processing |
| **numpy** | Numerical computations and matrix operations |
| **joblib** | Model serialization and persistence |

---

## Project Structure

This project resides inside the centralized internship workspace:

```text
Syntecxhub_Tasks/
│
├── Syntecxhub_Task1_AStar_Maze/
│
└── Syntecxhub_Sentiment_Analysis_Tool/
    ├── sentiment.py         # Main ML engine implementation
    ├── requirements.txt     # Project dependencies
    ├── .gitignore           # Git exclusion rules
    └── README.md            # Project documentation
```

---

## Installation & Local Setup

### 1️⃣ Navigate to the Project Directory

```bash
cd Syntecxhub_Tasks/Syntecxhub_Task2_Sentiment_Analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python sentiment.py
```

---

## ML Execution Workflow

### 1. NLP Preprocessing

Raw text undergoes multiple cleaning stages:

- Convert text to lowercase.
- Remove URLs and structural noise.
- Remove very short tokens.
- Filter stop words such as:

```text
the, and, for, is, are, ...
```

This ensures the model focuses on emotionally informative tokens.

---

### 2. Feature Extraction

The cleaned text is transformed into numerical vectors using one of two approaches:

#### **Count Vectorizer**

Converts text into raw token-frequency counts.

#### **TF-IDF Vectorizer**

Weights tokens according to their importance by emphasizing unique terms while down-weighting overly common words.

---

### 3. Model Training & Persistence

The dataset is split using a **stratified 80/20 train-test distribution**.

After training, the application allows the model and preprocessing pipeline to be saved for future inference.

```python
model_data = {
    'model': self.model,
    'vectorizer': self.vectorizer,
    'vectorizer_type': self.vectorizer_type,
    'classifier_type': self.classifier_type
}
```

---

## Sample Evaluation Output

```text
============================================================
 MODEL EVALUATION RESULTS
============================================================

 Accuracy:  0.9600
 F1 Score:  0.9592

 Classification Report:

              precision    recall  f1-score   support

Negative (0)       0.98      0.94      0.96        50
Positive (1)       0.94      0.98      0.96        50

    accuracy                           0.96       100
   macro avg       0.96      0.96      0.96       100
weighted avg       0.96      0.96      0.96       100

============================================================
```

---

## 🎓 Internship Information

This project was developed as **Task 2** during the **Artificial Intelligence Internship** at **Syntecxhub**.

---

## 👩‍💻 Author

<div align="center">

### **Aqsa Jamali**

**AI Intern @ Syntecxhub**

[![GitHub](https://img.shields.io/badge/GitHub-AqsaAliRazaJamali-181717?style=for-the-badge&logo=github)](https://github.com/AqsaAliRazaJamali)

</div>

---

## 📄 License

This project was developed exclusively for **academic learning and internship evaluation purposes** under the **Syntecxhub AI Internship Program**.

---

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
