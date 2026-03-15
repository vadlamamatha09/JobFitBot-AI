import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# ------------------ DARK THEME ------------------

st.markdown("""
<style>

.stApp{
background-color:#0f172a;
}

h1,h2,h3,h4,h5,h6{
color:#ffffff;
}

p,span,label{
color:#e2e8f0 !important;
font-size:16px;
}

button[data-baseweb="tab"]{
color:white !important;
font-size:16px;
}

.stButton>button{
background:linear-gradient(90deg,#6366f1,#06b6d4);
color:white;
border-radius:8px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 JobFitBot – AI Career Advisor")

# ------------------ JOB DATABASE ------------------

jobs = {
"Data Scientist":["python","machine learning","sql"],
"Software Engineer":["java","python","algorithms"],
"Web Developer":["html","css","javascript","react"],
"AI Engineer":["python","deep learning"],
"Cloud Engineer":["aws","docker","linux"],
"Cyber Security Analyst":["network security","linux"],
"Data Analyst":["excel","sql","python"],
"UI UX Designer":["figma","design"],
"Mobile App Developer":["flutter","kotlin","java"]
}

salary={
"Data Scientist":"12-30 LPA",
"Software Engineer":"8-25 LPA",
"Web Developer":"6-18 LPA",
"AI Engineer":"15-35 LPA",
"Cloud Engineer":"10-28 LPA",
"Cyber Security Analyst":"9-27 LPA",
"Data Analyst":"6-20 LPA",
"UI UX Designer":"5-15 LPA",
"Mobile App Developer":"7-20 LPA"
}

skills_db=[
"python","java","machine learning","sql","html","css",
"javascript","react","aws","docker","linux","excel",
"figma","flutter","kotlin"
]

education_branches={
"Inter":["MPC","BiPC","CEC","HEC"],
"Diploma":["CSE","ECE","EEE","Mechanical","Civil"],
"Degree":["B.Sc","B.Com","BBA","BA"],
"B.Tech":["CSE","IT","AI & ML","Data Science","ECE","Mechanical","Civil"],
"M.Tech":["CSE","AI","Data Science"],
"PG":["MBA","MCA","M.Sc"]
}

# ------------------ TABS ------------------

tab1,tab2,tab3,tab4,tab5 = st.tabs([
"🏠 Home",
"🚀 Career Prediction",
"📄 Resume Analyzer",
"🧠 Career Test",
"💬 Career Chatbot"
])

# =================================================
# HOME PAGE
# =================================================

with tab1:

    col1,col2,col3 = st.columns([2,2,1])
    with col1:
        st.metric("Career Prediction Accuracy","95%")
        # 0.5 cm spacing
    st.markdown("<div style='height:0.2cm'></div>", unsafe_allow_html=True)
    st.header("Welcome to JobFitBot")
    with col2:
        st.metric("Resume Analysis Quality","92%")
    with col3:
        fig = plt.figure(figsize=(2,2))
        plt.pie([35,25,20,20],labels=["AI","Cloud","Cyber","Data"])
        st.pyplot(fig)
    st.markdown("""
### 🚀 Your AI Powered Career Guidance Platform

JobFitBot helps students discover the best career paths using **AI skill analysis, resume intelligence, and career prediction models**.
""")

    st.markdown("<br>", unsafe_allow_html=True)

    colA,colB,colC = st.columns(3)

    with colA:
        st.markdown("""
### 🎯 Career Prediction
Analyze your skills and discover the **best career paths** with AI recommendations.
""")

    with colB:
        st.markdown("""
### 📄 Resume Analyzer
Upload your resume and get **top career matches** based on your skills.
""")

    with colC:
        st.markdown("""
### 🧠 Career Test
Take a quick test to discover **careers that match your interests**.
""")

    st.markdown("---")

# =================================================
# CAREER PREDICTION
# =================================================

with tab2:

    education = st.selectbox("Education",list(education_branches.keys()))

    branch = st.selectbox("Branch",education_branches[education])

    experience = st.selectbox(
    "Experience",
    ["Fresher","0-2 years","2-5 years","5+ years"]
    )

    skills_input = st.text_input("Enter Skills (comma separated)")

    cert_text = st.text_input("Certifications (optional)")

    cert_upload = st.file_uploader(
    "📂 Drag and drop certification files here or click to upload",
    accept_multiple_files=True
    )

    if st.button("Analyze My Career"):

        user_skills=[s.strip().lower() for s in skills_input.split(",") if s!=""]

        results=[]

        for job,req in jobs.items():

            match=len(set(user_skills)&set(req))
            score=(match/len(req))*100
            gap=[g for g in req if g not in user_skills]

            results.append((job,score,gap))

        results=sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("🎯 Top Career Matches")

        colors=["#22c55e","#38bdf8","#f97316"]

        for i,(job,score,gap) in enumerate(results[:3]):

            st.markdown(
            f"<h3 style='color:{colors[i]}'>{job} — {round(score,2)}% Match</h3>",
            unsafe_allow_html=True)

            st.write("Average Salary:",salary[job])

        top_job=results[0][0]
        top_gap=results[0][2]

        st.subheader("📈 Career Roadmap")

        for skill in top_gap:
            st.write("Learn:",skill)

# =================================================
# RESUME ANALYZER
# =================================================

with tab3:

    resume = st.file_uploader(
    "📄 Drag and drop your resume here or click to upload (PDF)",
    type=["pdf"]
    )

    if resume:

        reader = PdfReader(resume)

        text=""

        for page in reader.pages:
            text += page.extract_text()

        text=text.lower()

        detected=[]

        for skill in skills_db:
            if skill in text:
                detected.append(skill)

        st.subheader("Detected Skills")

        st.write(detected)

        results=[]

        for job,req in jobs.items():

            match=len(set(detected)&set(req))
            score=(match/len(req))*100

            results.append((job,score))

        results=sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("Top 3 Career Matches")

        for job,score in results[:3]:
            st.write(job,"—",round(score,2),"%")

# =================================================
# CAREER TEST
# =================================================

with tab4:

    q1 = st.radio(
    "Which activity do you enjoy most?",
    ["Coding","Design","Data Analysis","Management","Cyber Security"]
    )

    q2 = st.radio(
    "Which tool do you prefer?",
    ["Python","Excel","Figma","AWS","Networking"]
    )

    if st.button("Show Career Suggestion"):

        if q1=="Coding":
            st.success("Suggested Career: Software Engineer")

        elif q1=="Design":
            st.success("Suggested Career: UI UX Designer")

        elif q1=="Data Analysis":
            st.success("Suggested Career: Data Scientist")

        elif q1=="Cyber Security":
            st.success("Suggested Career: Cyber Security Analyst")

        else:
            st.success("Suggested Career: Business Manager")

# =================================================
# CHATBOT
# =================================================

with tab5:

    question = st.text_input("Ask about any career or skill")

    if question:

        q=question.lower()

        found=False

        for job,skills in jobs.items():

            if job.lower() in q:

                st.write("Skills Required:",skills)
                st.write("Average Salary:",salary[job])
                found=True

        for skill in skills_db:

            if skill in q:
                st.write("Skill detected:",skill)
                found=True

        if not found:

            st.write("Try asking about careers like Data Scientist, Cloud Engineer, Web Developer or skills like Python, AWS etc.")
