import streamlit as st
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from question_generator import generate_questions

st.set_page_config(page_title="AI Interview Question Generator", layout="centered")

st.title("AI Interview Question Generator from Resume")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing your resume..."):
        text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(text)
        questions = generate_questions(skills)

    st.subheader("✅ Extracted Skills")
    if skills:
        st.write(skills)
    else:
        st.write("No skills detected. Try another resume.")

    st.subheader("🧠 Generated Interview Questions")
    if questions:
        for q in questions:
            st.write("•", q)
    else:
        st.write("No questions generated.")