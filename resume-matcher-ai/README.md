# 🚀 AI Resume Intelligence Platform

An advanced AI-powered system that analyzes resumes against job descriptions and provides intelligent insights such as match score, skill gaps, resume improvements, and auto-generated cover letters.

---

## 📌 Overview

This project simulates a real-world **ATS (Applicant Tracking System)** used by companies to screen candidates efficiently. It uses NLP techniques to evaluate how well a resume matches a given job description.

---

## ✨ Features

### 📊 Resume Analysis

* Match Score using TF-IDF + Cosine Similarity
* Skill Coverage percentage
* Matched Skills vs Missing Skills

### 📄 Resume Insights

* Keyword highlighting
* Resume readability analysis

### ✍ AI Resume Rewriter

* Improves resume sentences
* Converts weak verbs into strong action verbs

### ✉ Cover Letter Generator

* Generates job-specific professional cover letter

### 📥 AI Report Download

* Download complete analysis as PDF

### 🎨 UI Features

* Dark / Light mode toggle
* Clean tab-based UI
* Skill badge visualization

---

## 🧠 Tech Stack

* Python
* Streamlit
* Scikit-learn (TF-IDF, Cosine Similarity)
* PDFPlumber
* ReportLab

---

## ⚙️ How It Works

1. Resume and job description are converted into vectors using TF-IDF.
2. Cosine similarity calculates how closely they match.
3. Skills are extracted using keyword mapping.
4. The system generates insights including score, skill gaps, and suggestions.

---

## 🧠 System Architecture

```
User Input (Resume + Job Description)
        ↓
PDF/Text Extraction
        ↓
Text Preprocessing & Cleaning
        ↓
Feature Extraction (TF-IDF)
        ↓
Similarity Computation (Cosine Similarity)
        ↓
Skill Extraction & Comparison
        ↓
Analysis Engine
        ↓
Output (Score, Skills, Suggestions, Report)
```

---

## ⚙️ Working Flow

### 1. Input Layer

* Resume upload (PDF or text)
* Job description input

### 2. Preprocessing

* Extract text using pdfplumber
* Clean and normalize text

### 3. Feature Extraction

* Convert text into vectors using TF-IDF

### 4. Matching

* Compute similarity using cosine similarity

### 5. Skill Analysis

* Identify matched and missing skills

### 6. AI Enhancements

* Resume rewriter improves sentences
* Cover letter generator creates professional output

### 7. Output

* Displays score, insights, suggestions
* Generates downloadable PDF report

---

## 📸 Screenshots

### 🏠 Home Page

![Home](Screenshots/home.png)

---

### 📊 Analysis Dashboard

![Analysis](Screenshots/analysis.png)

---

### 📄 Resume Insights

![Insights](Screenshots/insights.png)

---

### ✍ Resume Rewriter

![Rewriter](Screenshots/report.png)

---

### ✉ Cover Letter Generator

![Cover Letter](Screenshots/cover_letter.png)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Future Enhancements

* Integration with **Vector Databases (Endee)** for scalable similarity search
* Use of transformer-based embeddings
* Multi-job comparison feature
* Improved ATS scoring model

---

## 👩‍💻 Author

**Darshini ML**
BE CSE | ACS College of Engineering
CGPA: 9.1

📧 [mldarshini933@gmail.com](mailto:mldarshini933@gmail.com)
🔗 https://www.linkedin.com/in/darshini-ml
💻 https://github.com/Darshiniml

---

## ⭐ Conclusion

This project demonstrates how AI and NLP can be applied to automate resume screening and provide meaningful insights, making it useful for both job seekers and recruiters.
