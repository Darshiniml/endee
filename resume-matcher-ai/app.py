import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

st.title("AI Resume Matcher using Endee Vector Database")

resume = st.text_area("Paste Resume Text")
job_desc = st.text_area("Paste Job Description")

if st.button("Check Match"):
    if resume and job_desc:
        resume_vec = model.encode(resume)
        job_vec = model.encode(job_desc)

        score = cosine_similarity([resume_vec], [job_vec])[0][0]

        st.success(f"Match Score: {round(score*100,2)} %")
    else:
        st.warning("Please enter both Resume and Job Description.")
