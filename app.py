import streamlit as st
import pandas as pd

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- COLORFUL BACKGROUND ----------

st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg,#6dd5ed,#2193b0);
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 JobFitBot – AI Career Advisor")
st.write("AI Based Career Guidance and Skill Gap Analyzer")

# ---------- USER INPUT ----------

education = st.selectbox(
"Select Your Education",
["B.Tech","Degree","MBA","M.Tech","Diploma","Other"]
)

branch = st.selectbox(
"Select Branch / Field",
["Computer Science","Information Technology","Electronics","Mechanical","Civil","AI & ML","Data Science","Other"]
)

skills_input = st.text_input(
"Enter your skills (comma separated)",
"python, sql"
)

experience = st.selectbox(
"Experience Level",
["Fresher","0-2 years","2-5 years","5+ years"]
)

# ---------- JOB DATABASE ----------

jobs = {
"Data Scientist":["python","machine learning","statistics","sql","pandas"],
"Software Engineer":["java","python","data structures","algorithms","oop"],
"Web Developer":["html","css","javascript","react","node"],
"AI Engineer":["python","deep learning","tensorflow","nlp","pytorch"],
"Data Analyst":["excel","sql","python","powerbi","statistics"],
"Cyber Security Analyst":["network security","linux","python","cryptography"],
"Cloud Engineer":["aws","docker","kubernetes","linux"],
"Mobile App Developer":["flutter","dart","java","android"],
"DevOps Engineer":["docker","kubernetes","aws","linux","ci/cd"]
}

# ---------- ANALYSIS ----------

if st.button("Analyze My Career"):

    user_skills = [s.strip().lower() for s in skills_input.split(",")]

    results = []

    for job,req_skills in jobs.items():

        matched = len(set(user_skills) & set(req_skills))

        score = (matched/len(req_skills))*100

        skill_gap = list(set(req_skills) - set(user_skills))

        results.append((job,score,skill_gap))

    results = sorted(results,key=lambda x:x[1],reverse=True)

    st.subheader("🎯 Top Career Matches")

    for job,score,skill_gap in results[:5]:

        st.write("###",job)

        st.progress(int(score))

        st.write(f"Match Score: {score:.2f}%")

        if score>70:
            st.success("You are job ready for this role!")

        elif score>40:
            st.warning("You need some skill improvement.")

        else:
            st.error("You need major skill development.")

        if skill_gap:
            st.write("📚 Skills to Improve:")

            for s in skill_gap[:4]:
                st.write("-",s)

        st.write("---")

# ---------- CAREER ROADMAP ----------

st.subheader("📈 Career Growth Roadmap")

roadmap = {
"Data Scientist":["Learn Python","Study Statistics","Practice ML","Build Projects","Apply Jobs"],
"Web Developer":["Learn HTML/CSS","JavaScript","React","Build Websites","Apply Jobs"],
"AI Engineer":["Python","Deep Learning","TensorFlow","AI Projects","Apply Jobs"],
"Cloud Engineer":["Linux","AWS","Docker","Kubernetes","DevOps"]
}

role = st.selectbox("Select Role for Roadmap",list(roadmap.keys()))

if st.button("Show Roadmap"):

    steps = roadmap[role]

    for i,step in enumerate(steps):

        st.write(f"Step {i+1}:",step)

# ---------- RESUME TIPS ----------

st.subheader("📄 Resume Improvement Tips")

st.write("""
✔ Add projects related to your target job  
✔ Include certifications  
✔ Highlight technical skills clearly  
✔ Add internship experience  
✔ Use measurable achievements
""")

# ---------- FOOTER ----------

st.write("---")
st.write("JobFitBot – AI Career Advisor | Final Year Project")
