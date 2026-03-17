import streamlit as st
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

st.set_page_config(page_title="AI Resume Intelligence", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("AI Resume Intelligence")
dark_mode = st.sidebar.toggle("🌗 Dark Mode")

# ---------------- THEME ----------------
bg = "#0E1117" if dark_mode else "#f6f8fb"
text = "white" if dark_mode else "black"

st.markdown(f"""
<style>
.stApp {{
background-color:{bg};
color:{text};
}}

.skill-badge {{
display:inline-block;
padding:6px 12px;
margin:4px;
border-radius:20px;
background:#e3f2fd;
color:#0d47a1;
}}

.skill-missing {{
display:inline-block;
padding:6px 12px;
margin:4px;
border-radius:20px;
background:#ffebee;
color:#b71c1c;
}}

.highlight {{
background:#fff3cd;
padding:2px 6px;
border-radius:5px;
}}
</style>
""", unsafe_allow_html=True)

st.title("AI Resume Intelligence Platform")

# ---------------- FUNCTIONS ----------------
def extract_skills(text):
    text = text.lower()

    skill_map = {
        "java": "Java",
        "python": "Python",
        "sql": "SQL",
        "mysql": "SQL",
        "spring boot": "Spring Boot",
        "rest api": "REST API",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "machine learning": "Machine Learning",
        "react": "React",
        "microservices": "Microservices",
        "aws": "AWS",
        "git": "Git"
    }

    found = set()
    for key, value in skill_map.items():
        if key in text:
            found.add(value)

    return list(found)


def clean_resume_text(text):
    return re.sub(r'\(cid:\d+\)', '', text)


def highlight_keywords(text):
    for skill in extract_skills(text):
        text = re.sub(rf"\b({skill})\b",
                      r"<span class='highlight'>\1</span>",
                      text, flags=re.IGNORECASE)
    return text


def rewrite_resume_sentences(resume_text):
    resume_text = clean_resume_text(resume_text)
    lines = re.split(r'\n|–|-|•', resume_text)

    improvements = []

    for line in lines:
        line = line.strip()

        if len(line) < 30:
            continue

        if not any(w in line.lower() for w in ["developed","built","worked","used","created"]):
            continue

        improved = line
        improved = re.sub(r'\bDeveloped\b', 'Designed and implemented', improved)
        improved = re.sub(r'\bBuilt\b', 'Engineered', improved)
        improved = re.sub(r'\bWorked on\b', 'Contributed to development of', improved)
        improved = re.sub(r'\bUsed\b', 'Leveraged', improved)

        if improved != line:
            improvements.append((line, improved))

    return improvements


def generate_cover_letter(resume, job):
    return f"""Dear Hiring Manager,

I am excited to apply for this role.

With strong skills in {', '.join(extract_skills(resume))}, I believe I am a great fit for this position.

Sincerely,
Darshini ML
"""


def generate_report(sim, cov, matched, missing, cover):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Resume Report", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Match Score: {round(sim*100,2)}%", styles['Normal']))
    elements.append(Paragraph(f"Skill Coverage: {round(cov,2)}%", styles['Normal']))

    elements.append(Paragraph("Matched Skills:", styles['Heading2']))
    for s in matched:
        elements.append(Paragraph(s, styles['Normal']))

    elements.append(Paragraph("Missing Skills:", styles['Heading2']))
    for s in missing:
        elements.append(Paragraph(s, styles['Normal']))

    elements.append(Paragraph("Cover Letter:", styles['Heading2']))
    elements.append(Paragraph(cover, styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_file:
        with pdfplumber.open(uploaded_file) as pdf:
            resume = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume += text

        st.text_area("Extracted Resume", resume, height=200)

    else:
        resume = st.text_area("Paste Resume")

with col2:
    job = st.text_area("Paste Job Description", height=200)

# ---------------- ANALYSIS ----------------
if st.button("Analyze Resume"):

    if resume and job:

        tfidf = TfidfVectorizer().fit_transform([resume, job])
        sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

        res_skills = extract_skills(resume)
        job_skills = extract_skills(job)

        matched = sorted(set(res_skills) & set(job_skills))
        missing = sorted(set(job_skills) - set(res_skills))

        cov = (len(matched)/len(job_skills))*100 if job_skills else 0

        tabs = st.tabs(["📊 Analysis", "📄 Resume Insights", "✍ Rewriter", "✉ Cover Letter"])

        # ---------------- ANALYSIS TAB ----------------
        with tabs[0]:

            st.metric("Match Score", f"{round(sim*100,2)}%")
            st.metric("Skill Coverage", f"{round(cov,2)}%")

            colA, colB = st.columns(2)

            with colA:
                st.subheader("Matched Skills")
                if matched:
                    for s in matched:
                        st.markdown(f"<span class='skill-badge'>{s}</span>", unsafe_allow_html=True)
                else:
                    st.info("No matched skills")

            with colB:
                st.subheader("Missing Skills")

                if job_skills:
                    if missing:
                        for s in missing:
                            st.markdown(f"<span class='skill-missing'>{s}</span>", unsafe_allow_html=True)
                    else:
                        st.success("All skills matched 🎉")
                else:
                    st.warning("⚠ No skills detected in Job Description")

            st.subheader("Download Full AI Report")

            cover = generate_cover_letter(resume, job)
            pdf = generate_report(sim, cov, matched, missing, cover)

            st.download_button("Download Full AI Report (PDF)", pdf, "AI_Report.pdf")

        # ---------------- INSIGHTS TAB ----------------
        with tabs[1]:
            st.subheader("Resume Keyword Highlight")
            st.markdown(highlight_keywords(resume), unsafe_allow_html=True)

            st.subheader("Resume Readability")
            wc = len(resume.split())
            st.write(f"Word Count: {wc}")

            if wc < 200:
                st.warning("Too short")
            elif wc > 800:
                st.warning("Too long")
            else:
                st.success("Good length")

        # ---------------- REWRITER TAB ----------------
        with tabs[2]:
            st.subheader("AI Resume Rewriter")

            suggestions = rewrite_resume_sentences(resume)

            if suggestions:
                for o, i in suggestions:
                    st.info(o)
                    st.success(i)
            else:
                st.warning("No improvements detected.")

        # ---------------- COVER LETTER TAB ----------------
        with tabs[3]:
            st.subheader("Generated Cover Letter")

            cover = generate_cover_letter(resume, job)
            st.text_area("", cover, height=300)

    else:
        st.warning("Enter both resume and job description.")