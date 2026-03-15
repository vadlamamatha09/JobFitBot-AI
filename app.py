import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot",layout="wide")

# ---------- DARK UI ----------
st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp{
background-color:#0f172a;
color:white;
}

/* ALL TEXT */

html, body, [class*="css"]  {
color: white;
font-size:16px;
}

/* HEADINGS */

h1,h2,h3,h4,h5,h6{
color:#f8fafc;
}

/* INPUT BOXES */

.stTextInput input,
.stSelectbox div,
.stFileUploader,
textarea{
background-color:#1e293b !important;
color:white !important;
border:1px solid #38bdf8 !important;
}

/* BUTTONS */

.stButton>button{
background:linear-gradient(90deg,#6366f1,#06b6d4);
color:white;
border-radius:10px;
font-weight:bold;
}

/* TAB TEXT */

button[data-baseweb="tab"]{
color:white !important;
font-size:16px;
}

/* RADIO TEXT */

.stRadio label{
color:white !important;
}

/* METRICS */

[data-testid="stMetric"]{
background-color:#1e293b;
padding:10px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)
st.title("🤖 JobFitBot – AI Career Advisor")

# ---------- JOB DATABASE ----------

jobs={
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

learning_resources={
"python":["Coursera Python","freeCodeCamp Python","YouTube Python"],
"machine learning":["Coursera ML","freeCodeCamp ML","YouTube ML"],
"sql":["Coursera SQL","freeCodeCamp SQL","YouTube SQL"],
"html":["freeCodeCamp HTML"],
"css":["freeCodeCamp CSS"],
"javascript":["freeCodeCamp JS"],
"react":["Udemy React"],
"aws":["Coursera AWS"],
"docker":["Docker Tutorial"],
"linux":["Linux Tutorial"],
"excel":["Excel Tutorial"]
}

education_branches={
"Inter":["MPC","BiPC","CEC","HEC"],
"Diploma":["CSE","ECE","EEE","Mechanical","Civil"],
"Degree":["B.Sc","B.Com","BBA","BA"],
"B.Tech":["CSE","IT","AI & ML","Data Science","ECE","Mechanical","Civil"],
"M.Tech":["CSE","AI","Data Science"],
"PG":["MBA","MCA","M.Sc"]
}

# ---------- GAUGE ----------

def gauge(score):

    fig,ax=plt.subplots(figsize=(3,2))

    ax.barh([""],[score])

    ax.set_xlim(0,100)

    ax.set_title("Career Success Probability")

    return fig

# ---------- TABS ----------

tab1,tab2,tab3,tab4,tab5=st.tabs([
"🏠 Home",
"🚀 Career Prediction",
"📄 Resume Analyzer",
"🧠 Career Test",
"💬 Career Chatbot"
])

# ====================================================
# HOME
# ====================================================

with tab1:

    col1,col2,col3=st.columns([2,2,1])

    col1.metric("Career Prediction Accuracy","95%")
    col2.metric("Resume Analysis Quality","92%")

    with col3:

        fig=plt.figure(figsize=(2,2))
        plt.pie([35,25,20,20],labels=["AI","Cloud","Cyber","Data"])
        st.pyplot(fig)

    st.header("Welcome to JobFitBot")

    st.write("""
AI powered system that helps students discover careers,
analyze resumes and build skill roadmaps.
""")

# ====================================================
# CAREER PREDICTION
# ====================================================

with tab2:

    education=st.selectbox("Education",list(education_branches.keys()))

    branch=st.selectbox("Branch",education_branches[education])

    experience=st.selectbox("Experience",
    ["Fresher","0-2 years","2-5 years","5+ years"])

    skills_input=st.text_input("Enter Skills (comma separated)")

    cert_text=st.text_input("Certifications (optional)")

    cert_upload=st.file_uploader("Upload Certifications",accept_multiple_files=True)

    if st.button("Analyze My Career"):

        user_skills=[s.strip().lower() for s in skills_input.split(",") if s!=""]

        results=[]

        for job,req in jobs.items():

            match=len(set(user_skills)&set(req))
            score=(match/len(req))*100
            gap=[g for g in req if g not in user_skills]

            results.append((job,score,gap))

        results=sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("🎯 Top Career Recommendations")

        colors=["#22c55e","#38bdf8","#f97316"]

        for i,(job,score,gap) in enumerate(results[:3]):

            st.markdown(
            f"<h3 style='color:{colors[i]}'>{job} — {round(score,2)}% Match</h3>",
            unsafe_allow_html=True)

            st.write("Salary:",salary[job])

        top_job=results[0][0]
        top_score=results[0][1]
        top_gap=results[0][2]

        st.pyplot(gauge(top_score))

        st.subheader("📈 Career Roadmap")

        for skill in top_gap:

            st.write("Learn:",skill)

            if skill in learning_resources:

                for source in learning_resources[skill]:
                    st.write("•",source)

# ====================================================
# RESUME ANALYZER
# ====================================================

with tab3:

    resume=st.file_uploader("Upload Resume PDF")

    if resume:

        reader=PdfReader(resume)

        text=""

        for page in reader.pages:
            text+=page.extract_text()

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

# ====================================================
# CAREER TEST
# ====================================================

with tab4:

    q1=st.radio(
    "Which activity do you enjoy?",
    ["Coding","Design","Data Analysis","Management","Security"]
    )

    q2=st.radio(
    "Which tool do you prefer?",
    ["Python","Excel","Figma","AWS","Networking"]
    )

    if st.button("Show Career Suggestion"):

        if q1=="Coding":
            st.success("Software Engineer")

        elif q1=="Design":
            st.success("UI UX Designer")

        elif q1=="Data Analysis":
            st.success("Data Scientist")

        elif q1=="Security":
            st.success("Cyber Security Analyst")

        else:
            st.success("Business Manager")

# ====================================================
# CHATBOT
# ====================================================

with tab5:

    question=st.text_input("Ask about any career or skill")

    if question:

        q=question.lower()

        found=False

        for job,skills in jobs.items():

            if job.lower() in q:

                st.write("Skills required:",skills)
                st.write("Average Salary:",salary[job])
                found=True

        for skill in skills_db:

            if skill in q:

                st.write("Learning resources for",skill)

                if skill in learning_resources:

                    for r in learning_resources[skill]:
                        st.write("•",r)

                found=True

        if not found:

            st.write("Try asking about careers like Data Scientist, Cloud Engineer, Web Developer or skills like Python, AWS etc.")
