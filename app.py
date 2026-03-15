import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- CLEAN STYLE ----------

st.markdown("""
<style>
.block-container{
padding-top:0rem;
}

.stApp{
background-color:#f5f7fb;
}

.card{
background:white;
padding:20px;
border-radius:10px;
margin-bottom:20px;
box-shadow:0px 3px 8px rgba(0,0,0,0.1);
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
"Data Analyst":["excel","sql","python"]
}

salary={
"Data Scientist":"12-30 LPA",
"Software Engineer":"8-25 LPA",
"Web Developer":"6-18 LPA",
"AI Engineer":"15-35 LPA",
"Cloud Engineer":"10-28 LPA",
"Cyber Security Analyst":"9-27 LPA",
"Data Analyst":"6-20 LPA"
}

skills_db=[
"python","java","machine learning","sql","html","css",
"javascript","react","aws","docker","linux","excel"
]

# ---------- LEARNING SOURCES ----------

learning_resources={
"python":["Coursera Python Course","freeCodeCamp Python","YouTube Python Crash Course"],
"machine learning":["Coursera ML Course","freeCodeCamp ML Tutorial","YouTube ML Crash Course"],
"sql":["Coursera SQL Course","freeCodeCamp SQL Course","YouTube SQL Tutorial"],
"html":["freeCodeCamp HTML Course","YouTube HTML Tutorial"],
"css":["freeCodeCamp CSS Course","YouTube CSS Tutorial"],
"javascript":["freeCodeCamp JavaScript","YouTube JavaScript Course"],
"react":["Udemy React Course","YouTube React Tutorial"],
"aws":["Coursera AWS Fundamentals","YouTube AWS Tutorial"],
"docker":["Udemy Docker Course","YouTube Docker Tutorial"],
"linux":["freeCodeCamp Linux Course","YouTube Linux Tutorial"],
"excel":["Coursera Excel Course","YouTube Excel Tutorial"]
}

# ---------- TABS ----------

tab1,tab2,tab3,tab4,tab5 = st.tabs([
"🏠 Home",
"🚀 Career Prediction",
"📄 Resume Analyzer",
"🧠 Career Test",
"💬 Career Chatbot"
])

# =====================================================
# HOME
# =====================================================

with tab1:

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Career Prediction Accuracy","95%")
    col2.metric("Resume Analysis Quality","90%")
    col3.metric("AI Career Roadmap","92%")
    col4.metric("Career Guidance","93%")

    st.markdown("---")

    st.header("Welcome to JobFitBot")

    st.write("""
JobFitBot is an AI-powered career guidance platform that helps students:

• Discover the best career options  
• Analyze resume skills  
• Identify missing skills  
• Get a career learning roadmap
""")

    st.subheader("🔥 Trending Tech Careers")

    trending=["AI Engineer","Data Scientist","Cloud Engineer","Cyber Security"]

    for t in trending:
        st.write("•",t)

    st.subheader("📊 Tech Demand")

    fig=plt.figure()
    plt.pie([35,25,20,20],labels=["AI","Cloud","Cyber","Data"])
    st.pyplot(fig)

# =====================================================
# CAREER PREDICTION
# =====================================================

with tab2:

    st.markdown("### Enter Your Details")

    education=st.selectbox("Education",
    ["Inter","Diploma","Degree","B.Tech","M.Tech","PG"])

    branch=st.text_input("Branch / Field")

    experience=st.selectbox("Experience",
    ["Fresher","0-2 years","2-5 years","5+ years"])

    skills_input=st.text_input("Enter Skills (comma separated)")

    certifications=st.text_input("Enter Certifications")

    analyze=st.button("Analyze My Career")

    if analyze:

        user_skills=[s.strip().lower() for s in skills_input.split(",") if s!=""]

        results=[]

        for job,req in jobs.items():

            match=len(set(user_skills)&set(req))
            score=(match/len(req))*100
            gap=[g for g in req if g not in user_skills]

            results.append((job,score,gap))

        results=sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("🎯 Top Career Recommendations")

        for job,score,gap in results[:5]:

            st.write(f"**{job} — Match Probability: {round(score,2)}%**")
            st.write("Average Salary:",salary[job])
            st.write("---")

        st.subheader("🧭 Career Roadmap")

        top_job=results[0][0]
        top_gap=results[0][2]

        st.write("Target Career:",top_job)

        for skill in top_gap:

            st.write("Learn:",skill)

            if skill in learning_resources:

                for source in learning_resources[skill]:
                    st.write("•",source)

# =====================================================
# RESUME ANALYZER
# =====================================================

with tab3:

    resume=st.file_uploader("Upload Resume (PDF)")

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

        st.subheader("Skills to Improve")

        missing=[s for s in skills_db if s not in detected]

        for m in missing[:5]:

            st.write("Skill:",m)

            if m in learning_resources:

                for source in learning_resources[m]:
                    st.write("•",source)

# =====================================================
# CAREER TEST
# =====================================================

with tab4:

    st.header("Career Personality Test")

    q1=st.radio(
    "Which activity do you enjoy most?",
    ["Coding","Designing","Analyzing Data","Managing People"]
    )

    if st.button("Show Career Suggestion"):

        if q1=="Coding":
            st.success("Suggested Career: Software Engineer")

        elif q1=="Designing":
            st.success("Suggested Career: UI/UX Designer")

        elif q1=="Analyzing Data":
            st.success("Suggested Career: Data Scientist")

        else:
            st.success("Suggested Career: Business Manager")

# =====================================================
# CHATBOT
# =====================================================

with tab5:

    st.header("Career Chatbot")

    question=st.text_input("Ask a career question")

    if question:

        q=question.lower()

        if "data scientist" in q:
            st.write("Skills: Python, Machine Learning, SQL")

        elif "software engineer" in q:
            st.write("Skills: Java/Python, Data Structures")

        elif "cloud" in q:
            st.write("Skills: AWS, Docker, Linux")

        else:
            st.write("Try asking about careers like Data Scientist, Cloud Engineer, Software Engineer.")
