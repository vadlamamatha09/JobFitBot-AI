import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- BACKGROUND STYLE ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#1a2980,#26d0ce);
}

.main-box{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 0px 10px gray;
}

.small-chart{
width:400px;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.title("🤖 JobFitBot – AI Career Advisor")

st.write("AI powered career guidance platform for students")

st.write("---")

# ---------- INPUT SECTION ----------

st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.subheader("👤 Student Information")

col1,col2 = st.columns(2)

with col1:

    education = st.selectbox(
    "Education",
    [
    "B.Tech","B.Sc","B.Com","BA",
    "MBA","M.Tech","M.Sc",
    "Diploma","Polytechnic","Other"
    ]
    )

    branch = st.selectbox(
    "Branch / Field",
    [
    "Computer Science",
    "Information Technology",
    "AI & ML",
    "Data Science",
    "Electronics",
    "Mechanical",
    "Civil",
    "Electrical",
    "Business Administration",
    "Finance",
    "Marketing",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Other"
    ]
    )

with col2:

    experience = st.selectbox(
    "Experience Level",
    ["Fresher","0-2 years","2-5 years","5+ years"]
    )

skills_input = st.text_input(
"Enter your skills (comma separated)  (Optional)"
)

# ---------- RESUME ANALYZER ----------

st.subheader("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

resume_skills = []

skills_list = [
"python","java","machine learning","sql","excel",
"html","css","javascript","react","aws",
"docker","kubernetes","linux","tensorflow"
]

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            resume_skills.append(skill)

    st.success("Detected skills from resume:")

    st.write(resume_skills)

st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# ---------- COMBINE SKILLS ----------

skills_user = []

if skills_input:
    skills_user = [s.strip().lower() for s in skills_input.split(",")]

combined_skills = list(set(skills_user + resume_skills))

# ---------- JOB DATABASE ----------

jobs = {
"Data Scientist":["python","machine learning","statistics","sql","pandas"],
"Software Engineer":["java","python","data structures","algorithms"],
"Web Developer":["html","css","javascript","react"],
"AI Engineer":["python","deep learning","tensorflow","nlp"],
"Data Analyst":["excel","sql","python","powerbi"],
"Cloud Engineer":["aws","docker","kubernetes","linux"],
"Cyber Security Analyst":["network security","linux","python"],
"DevOps Engineer":["docker","kubernetes","aws","linux"],
"Mobile App Developer":["flutter","android","java"],
"UI UX Designer":["figma","design","prototyping"]
}

salary = {
"Data Scientist":"12-30 LPA",
"Software Engineer":"8-25 LPA",
"Web Developer":"6-18 LPA",
"AI Engineer":"15-35 LPA",
"Data Analyst":"6-20 LPA",
"Cloud Engineer":"10-28 LPA",
"Cyber Security Analyst":"9-27 LPA",
"DevOps Engineer":"12-30 LPA",
"Mobile App Developer":"7-20 LPA",
"UI UX Designer":"6-15 LPA"
}

# ---------- ANALYZE CAREER ----------

if st.button("🚀 Analyze My Career"):

    if len(combined_skills)==0:

        st.warning("Please enter skills or upload resume")

    else:

        results = []

        for job,req in jobs.items():

            matched = len(set(combined_skills) & set(req))
            score = (matched/len(req))*100
            gap = list(set(req)-set(combined_skills))

            results.append((job,score,gap))

        results = sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("🎯 Best Career Matches")

        for job,score,gap in results[:5]:

            st.write("###",job)

            st.progress(int(score))

            st.write("Match Score:",round(score,2),"%")

            st.info("💰 Average Salary: "+salary[job])

            if gap:
                st.write("📚 Skills to Improve:")
                for g in gap[:3]:
                    st.write("-",g)

            st.write("---")

# ---------- SMALL SKILL CHART ----------

if len(combined_skills)>0:

    st.subheader("📊 Your Skill Visualization")

    fig = plt.figure(figsize=(4,2))

    values = np.ones(len(combined_skills))

    plt.bar(combined_skills,values)

    plt.xticks(rotation=45)

    st.pyplot(fig)

# ---------- SMALL JOB DEMAND CHART ----------

demand = {
"AI Engineer":95,
"Data Scientist":90,
"Cloud Engineer":88,
"Cyber Security":87,
"DevOps":86
}

st.subheader("📈 Trending Tech Careers")

fig2 = plt.figure(figsize=(4,2))

plt.barh(list(demand.keys()),list(demand.values()))

st.pyplot(fig2)

# ---------- CAREER CHATBOT ----------

st.subheader("🤖 AI Career Assistant")

question = st.text_input("Ask any career question")

if question:

    st.success(
    "Focus on internships, real-world projects, and certifications to improve career opportunities."
    )

st.write("---")
st.write("JobFitBot – AI Career Advisor | Final Year Project")
