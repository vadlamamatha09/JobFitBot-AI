import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# -------- BACKGROUND --------

st.markdown(
"""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1519389950473-47ba0277781c");
background-size: cover;
background-attachment: fixed;
}

.block-container{
background-color: rgba(255,255,255,0.88);
padding: 2rem;
border-radius: 15px;
}

h1{
color:#1a237e;
}

</style>
""",
unsafe_allow_html=True
)

# -------- TITLE --------

st.title("🤖 JobFitBot – AI Career Advisor")

st.write(
"Discover the best career path using AI powered skill analysis, resume evaluation, and market demand prediction."
)

st.write("---")

# -------- USER INPUT --------

col1, col2 = st.columns(2)

with col1:

    education = st.selectbox(
    "Education",
    ["B.Tech","Degree","MBA","M.Tech","Diploma","Other"]
    )

    branch = st.selectbox(
    "Branch",
    ["Computer Science","Information Technology","Electronics","Mechanical","Civil","AI & ML","Data Science","Other"]
    )

with col2:

    experience = st.selectbox(
    "Experience Level",
    ["Fresher","0-2 years","2-5 years","5+ years"]
    )

skills_input = st.text_input(
"Enter your skills (comma separated)",
"python, sql"
)

# -------- JOB DATABASE --------

jobs = {
"Data Scientist":["python","machine learning","statistics","sql","pandas"],
"Software Engineer":["java","python","data structures","algorithms"],
"Web Developer":["html","css","javascript","react"],
"AI Engineer":["python","deep learning","tensorflow","nlp"],
"Data Analyst":["excel","sql","python","powerbi"],
"Cloud Engineer":["aws","docker","kubernetes","linux"],
"Cyber Security Analyst":["network security","linux","python"],
"DevOps Engineer":["docker","kubernetes","aws","linux"]
}

salary = {
"Data Scientist":"12 LPA - 30 LPA",
"Software Engineer":"8 LPA - 25 LPA",
"Web Developer":"6 LPA - 18 LPA",
"AI Engineer":"15 LPA - 35 LPA",
"Data Analyst":"6 LPA - 20 LPA",
"Cloud Engineer":"10 LPA - 28 LPA",
"Cyber Security Analyst":"9 LPA - 27 LPA",
"DevOps Engineer":"12 LPA - 30 LPA"
}

demand = {
"Data Scientist":90,
"Software Engineer":85,
"Web Developer":75,
"AI Engineer":95,
"Data Analyst":80,
"Cloud Engineer":88,
"Cyber Security Analyst":87,
"DevOps Engineer":86
}

# -------- CAREER ANALYSIS --------

if st.button("Analyze My Career"):

    user_skills = [i.strip().lower() for i in skills_input.split(",")]

    results = []

    for job,req in jobs.items():

        matched = len(set(user_skills) & set(req))
        score = (matched/len(req))*100

        gap = list(set(req) - set(user_skills))

        results.append((job,score,gap))

    results = sorted(results,key=lambda x:x[1],reverse=True)

    st.subheader("🎯 Best Career Matches")

    for job,score,gap in results[:5]:

        st.write("###",job)

        st.progress(int(score))

        st.write("Match Score:",round(score,2),"%")

        st.info("💰 Average Salary: " + salary[job])

        st.write("📈 Market Demand:",demand[job],"%")

        if gap:

            st.write("📚 Skills to Learn:")

            for g in gap[:4]:
                st.write("-",g)

        st.write("---")

# -------- SKILL VISUALIZATION --------

st.subheader("📊 Skill Visualization")

if st.button("Show Skill Chart"):

    user_skills = [i.strip() for i in skills_input.split(",")]

    values = np.ones(len(user_skills))

    fig = plt.figure()

    plt.bar(user_skills,values)

    plt.title("Your Skill Set")

    st.pyplot(fig)

# -------- RESUME ANALYZER --------

st.subheader("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

skills_list = [
"python","java","machine learning","sql","excel",
"html","css","javascript","aws","docker","react"
]

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    st.write("Detected Skills:")

    st.success(found)

# -------- JOB MARKET DEMAND --------

st.subheader("📈 Job Market Demand")

roles = list(demand.keys())
values = list(demand.values())

fig2 = plt.figure()

plt.barh(roles,values)

plt.title("Technology Job Demand")

st.pyplot(fig2)

# -------- AI CAREER CHAT --------

st.subheader("🤖 AI Career Assistant")

question = st.text_input("Ask any career question")

if question:

    st.write("AI Suggestion:")

    st.success(
    "Focus on building strong technical projects, internships, and certifications to increase employability."
    )

st.write("---")
st.write("JobFitBot – AI Career Advisor | Final Year Project")
