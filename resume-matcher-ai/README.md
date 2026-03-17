# AI Resume Matcher using Endee Vector Database

## Overview
This project demonstrates an AI-powered Resume–Job Description matching system.  
It uses vector representations of text to compute similarity between resumes and job descriptions.

The system is designed following the architecture of the Endee Vector Database for efficient semantic search.

## Features
- Resume semantic similarity matching
- Skill extraction from resume
- Missing skill detection
- Vector-based document comparison
- AI-powered job matching

## Technology Stack
- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Endee Vector Database (Architecture Integration)

## System Architecture

User Input (Resume + Job Description)
        ↓
Text Preprocessing
        ↓
Vector Embedding Generation
        ↓
Endee Vector Database
        ↓
Vector Similarity Search
        ↓
Match Score + Skill Analysis

## How It Works
1. The user inputs a resume and job description.
2. Text is converted into vector embeddings.
3. These vectors represent the semantic meaning of the text.
4. Similarity search is performed to calculate the match score.
5. The system identifies matched and missing skills.

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

python -m streamlit run app.py

Open the browser:

http://localhost:8501

## Example Output

Match Score: 82%

Matched Skills:
- Java
- REST API
- SQL

Missing Skills:
- Docker
- Kubernetes
