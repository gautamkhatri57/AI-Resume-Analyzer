import streamlit as st
import pandas as pd
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    skills = pd.read_csv("skills.csv")

    found_skills = []

    for skill in skills["skill"]:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    score = (len(found_skills) / len(skills)) * 100

    st.subheader("Detected Skills")
    st.write(found_skills)

    st.subheader("Resume Score")
    st.success(f"{score:.2f}%")

    missing = list(
        set(skills["skill"]) - set(found_skills)
    )

    st.subheader("Missing Skills")
    st.write(missing)