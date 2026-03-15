import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from streamlit_echarts import st_echarts

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- UI STYLE ----------

st.markdown("""
<style>
.block-container{
padding-top:0rem;
}

.stApp{
background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
color:white;
}

button[data-baseweb="tab"]{
color:white;
font-size:18px;
}

.card{
background:rgba(255,255,255,0.9);
padding:20px;
border-radius:12px;
margin-bottom:20px;
color:black;
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

learning_resources = {

"python":[
"Coursera - Python for Everybody",
"freeCodeCamp - Python Full Course",
"YouTube - Python Crash Course"
],

"machine learning":[
"Coursera - Machine Learning by Andrew Ng",
"freeCodeCamp - Machine Learning Tutorial",
"YouTube - Machine Learning Crash Course"
],

"sql":[
"Coursera - SQL for Data Science",
"freeCodeCamp - SQL Tutorial",
"YouTube - SQL Full Course"
],

"html":[
"freeCodeCamp - HTML Course",
"YouTube - HTML Crash Course"
],

"css":[
"freeCodeCamp - CSS Course",
"YouTube - CSS Tutorial"
],

"javascript":[
"freeCodeCamp - JavaScript Course",
"YouTube - JavaScript Tutorial"
],

"react":[
"Udemy - React Bootcamp",
"YouTube - React Tutorial"
],

"aws":[
"Coursera - AWS Fundamentals",
"YouTube - AWS Tutorial"
],

"docker":[
"Udemy - Docker Mastery",
"YouTube - Docker Tutorial"
],

"linux":[
"freeCodeCamp - Linux Course",
"YouTube - Linux Tutorial"
],

"excel":[
"Coursera - Excel Skills for Business",
"YouTube - Excel Tutorial"
]

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

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.header("Welcome to JobFitBot")

    st.write("""
JobFitBot is an AI powered career guidance platform that helps students:

✔ Discover best career paths  
✔ Analyze skills and resume  
✔ Identify missing skills  
✔ Generate AI career roadmap  
✔ Improve resume quality
""")

    st.subheader("🔥 Trending Tech Careers")

    trending=["AI Engineer","Data Scientist","Cloud Engineer","Cyber Security"]

    for t in trending:
        st.write("•",t)

    st.markdown('</div>',unsafe_allow_html=True)

# =====================================================
# CAREER PREDICTION
# =====================================================

with tab2:

    col1,col2 = st.columns([3,1])

    with col1:

        st.markdown('<div class="card">',unsafe_allow_html=True)

        education=st.selectbox(
        "Education",
        ["Inter","Diploma","Degree","B.Tech","M.Tech","PG"]
        )

        if education=="Inter":
            branches=["MPC","BiPC","CEC"]

        elif education=="Diploma":
            branches=["CSE","ECE","EEE","Mechanical","Civil"]

        elif education=="Degree":
            branches=["B.Sc","B.Com","BA","BBA"]

        elif education=="B.Tech":
            branches=["CSE","IT","AI & ML","Data Science","ECE"]

        elif education=="M.Tech":
            branches=["CSE","AI","Data Science"]

        else:
            branches=["MBA","MCA","M.Sc"]

        branch=st.selectbox("Branch / Field",branches)

        experience=st.selectbox(
        "Experience",
        ["Fresher","0-2 years","2-5 years","5+ years"]
        )

        skills_input=st.text_input(
        "Enter Skills (comma separated)"
        )

        certifications=st.text_input(
        "Enter Certifications"
        )

        cert_upload=st.file_uploader(
        "Upload Certificates",
        accept_multiple_files=True
        )

        analyze=st.button("🚀 Analyze My Career")

        st.markdown('</div>',unsafe_allow_html=True)

    # ---------- SIDE CHARTS ----------

    with col2:

        st.subheader("Skill Chart")

        if skills_input:

            skills=[s.strip() for s in skills_input.split(",")]

            fig=plt.figure(figsize=(2,2))
            plt.pie([1]*len(skills),labels=skills)
            st.pyplot(fig)

        st.subheader("Tech Demand")

        fig2=plt.figure(figsize=(2,2))
        plt.pie([35,25,20,20],labels=["AI","Cloud","Cyber","Data"])
        st.pyplot(fig2)

    if analyze:

        user_skills=[s.strip().lower() for s in skills_input.split(",") if s!=""]

        results=[]

        for job,req in jobs.items():

            match=len(set(user_skills)&set(req))
            score=(match/len(req))*100
            gap=[g for g in req if g not in user_skills]

            results.append((job,score,gap))

        results=sorted(results,key=lambda x:x[1],reverse=True)

        st.subheader("📊 AI Career Dashboard")

        resume_score=min(len(user_skills)*10,100)
        career_match=int(results[0][1])
        skill_strength=min(len(user_skills)*10,100)
        readiness=int((resume_score+career_match)/2)

        col1,col2,col3,col4 = st.columns(4)

        def gauge(value,title):

            option = {
                "series":[
                    {
                        "type":"gauge",
                        "startAngle":90,
                        "endAngle":-270,
                        "progress":{"show":True},
                        "axisLine":{"lineStyle":{"width":10}},
                        "axisTick":{"show":False},
                        "splitLine":{"show":False},
                        "axisLabel":{"show":False},
                        "detail":{
                            "valueAnimation":True,
                            "formatter":"{value}%",
                            "fontSize":18
                        },
                        "data":[{"value":value,"name":title}]
                    }
                ]
            }

            return option

        with col1:
            st_echarts(gauge(resume_score,"Resume Score"),height="200px")

        with col2:
            st_echarts(gauge(career_match,"Career Match"),height="200px")

        with col3:
            st_echarts(gauge(skill_strength,"Skill Strength"),height="200px")

        with col4:
            st_echarts(gauge(readiness,"Job Readiness"),height="200px")

        st.subheader("🎯 Best Career Matches")

        for job,score,gap in results[:3]:

            st.markdown(f"""
            <div class="card">
            <h3>{job}</h3>
            <p>Match Score: {round(score,2)}%</p>
            <p>Salary: {salary[job]}</p>
            </div>
            """,unsafe_allow_html=True)

        st.subheader("🧭 AI Career Roadmap")

        top_job=results[0][0]
        top_gap=results[0][2]

        step=1

        for skill in top_gap:

            st.write(f"Step {step} – Learn {skill}")

            if skill in learning_resources:

                st.write("Learning Sources:")

                for source in learning_resources[skill]:
                    st.write("•",source)

            step+=1

# =====================================================
# RESUME ANALYZER
# =====================================================

with tab3:

    st.markdown('<div class="card">',unsafe_allow_html=True)

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

        st.success("Detected Skills")

        st.write(detected)

        st.subheader("Skills to Improve")

        missing=[s for s in skills_db if s not in detected]

        for m in missing[:5]:

            st.subheader(m)

            if m in learning_resources:

                for source in learning_resources[m]:
                    st.write("•",source)

    st.markdown('</div>',unsafe_allow_html=True)

# =====================================================
# CAREER TEST
# =====================================================

with tab4:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.header("Career Personality Test")

    q1=st.radio(
    "Which activity do you enjoy most?",
    ["Coding","Designing","Analyzing Data","Managing People"]
    )

    if st.button("Show Career"):

        if q1=="Coding":
            st.success("Suggested Career: Software Engineer")

        elif q1=="Designing":
            st.success("Suggested Career: UI/UX Designer")

        elif q1=="Analyzing Data":
            st.success("Suggested Career: Data Scientist")

        else:
            st.success("Suggested Career: Business Manager")

    st.markdown('</div>',unsafe_allow_html=True)

# =====================================================
# CHATBOT
# =====================================================

with tab5:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.header("💬 AI Career Chatbot")

    question=st.text_input("Ask career question")

    if question:

        q=question.lower()

        if "data scientist" in q:
            st.write("Skills required: Python, Machine Learning, SQL")

        elif "software engineer" in q:
            st.write("Skills required: Java/Python, DSA, System Design")

        elif "cloud" in q:
            st.write("Skills required: AWS, Docker, Linux")

        else:
            st.write("Try asking about careers like Data Scientist, Cloud Engineer, Software Engineer")

    st.markdown('</div>',unsafe_allow_html=True)
