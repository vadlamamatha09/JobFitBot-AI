import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- BACKGROUND STYLE ----------

st.markdown("""
<style>

body{
margin:0;
}

.stApp{
background-image:url("https://images.unsplash.com/photo-1581094794329-c8112a89af12");
background-size:cover;
background-repeat:no-repeat;
background-attachment:fixed;
}

.block-container{
padding-top:1rem;
}

.card{
background:rgba(255,255,255,0.93);
padding:20px;
border-radius:12px;
}

</style>
""",unsafe_allow_html=True)

st.title("🤖 JobFitBot – AI Career Advisor")

# ---------- TABS ----------

tab1,tab2,tab3,tab4 = st.tabs([
"🏠 Home",
"🚀 Career Prediction",
"📄 Resume Analyzer",
"🧠 Career Test"
])

# =====================================================
# HOME
# =====================================================

with tab1:

    col1,col2 = st.columns([3,1])

    with col1:

        st.markdown('<div class="card">',unsafe_allow_html=True)

        st.header("Welcome to JobFitBot")

        st.write("""
JobFitBot is an AI based career advisor platform that helps students:

✔ Discover best career roles  
✔ Analyze their skills and certifications  
✔ Detect skill gaps  
✔ Improve job readiness  
""")

        st.markdown('</div>',unsafe_allow_html=True)

    with col2:

        st.subheader("Skill Chart")

        fig = plt.figure(figsize=(2,2))
        plt.pie([30,25,20,25],
        labels=["Python","AI","Cloud","Web"],
        colors=["#ff6b6b","#6bc5ff","#ffe66d","#6bff95"])
        st.pyplot(fig)

        st.subheader("Tech Trends")

        fig2 = plt.figure(figsize=(2,2))
        plt.pie([35,25,20,20],
        labels=["AI","Cloud","Cyber","Data"],
        colors=["#8338ec","#3a86ff","#ff006e","#fb5607"])
        st.pyplot(fig2)

# =====================================================
# CAREER PREDICTION
# =====================================================

with tab2:

    col1,col2 = st.columns([3,1])

    with col1:

        st.markdown('<div class="card">',unsafe_allow_html=True)

        education = st.selectbox(
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
            branches=["CSE","IT","AI & ML","Data Science","ECE","Mechanical","Civil"]

        elif education=="M.Tech":
            branches=["CSE","AI","Data Science"]

        else:
            branches=["MBA","MCA","M.Sc"]

        branch = st.selectbox("Branch / Field",branches)

        experience = st.selectbox(
        "Experience",
        ["Fresher","0-2 years","2-5 years","5+ years"]
        )

        skills_input = st.text_input(
        "Enter Skills (comma separated)"
        )

        certifications = st.text_input(
        "Enter Certifications (optional)"
        )

        cert_upload = st.file_uploader(
        "Upload Certificates (optional)",
        accept_multiple_files=True
        )

        analyze = st.button("🚀 Analyze My Career")

        st.markdown('</div>',unsafe_allow_html=True)

    # ---------- SIDE CHARTS ----------

    with col2:

        st.subheader("Skill Chart")

        if skills_input:

            skills=[i.strip() for i in skills_input.split(",")]

            fig=plt.figure(figsize=(2,2))
            plt.pie([1]*len(skills),
            labels=skills,
            colors=["#ff6b6b","#4ecdc4","#ffe66d","#1a535c","#ff9f1c"])
            st.pyplot(fig)

        st.subheader("Tech Trends")

        fig2=plt.figure(figsize=(2,2))
        plt.pie(
        [30,25,25,20],
        labels=["AI","Cloud","Cyber","Data"],
        colors=["#8338ec","#3a86ff","#ff006e","#fb5607"]
        )
        st.pyplot(fig2)

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

    # ---------- ANALYSIS ----------

    if analyze:

        if skills_input=="":

            st.warning("Please enter skills")

        else:

            user_skills=[i.strip().lower() for i in skills_input.split(",")]

            results=[]

            for job,req in jobs.items():

                matched=len(set(user_skills)&set(req))
                score=(matched/len(req))*100
                gap=[skill for skill in req if skill not in user_skills]

                results.append((job,score,gap))

            results=sorted(results,key=lambda x:x[1],reverse=True)

            # ---------- DASHBOARD ----------

            st.subheader("📊 AI Career Dashboard")

            colA,colB,colC,colD = st.columns(4)

            resume_score=len(user_skills)*10
            if resume_score>100:
                resume_score=100

            career_match=int(results[0][1])

            skill_strength=len(user_skills)*10
            if skill_strength>100:
                skill_strength=100

            job_readiness=int((resume_score+career_match)/2)

            colA.metric("📄 Resume Score",str(resume_score)+"/100")
            colB.metric("🎯 Career Match",str(career_match)+"%")
            colC.metric("💡 Skill Strength",str(skill_strength)+"/100")
            colD.metric("🚀 Job Readiness",str(job_readiness)+"%")

            st.write("---")

            # ---------- BEST MATCHES ----------

            st.subheader("🎯 Best Career Matches")

            for job,score,gap in results[:5]:

                st.write("###",job)

                st.progress(int(score))

                st.write("Match Score:",round(score,2),"%")

                st.info("Salary Range: "+salary[job])

                if gap:

                    st.write("Skills to Improve")

                    for g in gap[:3]:
                        st.write("-",g)

                st.write("---")

# =====================================================
# RESUME ANALYZER
# =====================================================

with tab3:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.header("📄 Resume Analyzer")

    resume_file = st.file_uploader("Upload Resume (PDF)")

    skill_database=[
    "python","java","machine learning",
    "sql","html","css","javascript",
    "react","aws","docker","linux","excel"
    ]

    if resume_file:

        reader=PdfReader(resume_file)

        text=""

        for page in reader.pages:
            text+=page.extract_text()

        text=text.lower()

        found=[]

        for skill in skill_database:
            if skill in text:
                found.append(skill)

        st.success("Detected Skills")

        st.write(found)

    st.markdown('</div>',unsafe_allow_html=True)

# =====================================================
# CAREER TEST
# =====================================================

with tab4:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.header("🧠 Career Personality Test")

    q1=st.radio(
    "Which activity do you enjoy most?",
    ["Coding","Designing","Analyzing Data","Managing People"]
    )

    if st.button("Show Result"):

        if q1=="Coding":
            st.success("Recommended Career: Software Engineer")

        elif q1=="Designing":
            st.success("Recommended Career: UI/UX Designer")

        elif q1=="Analyzing Data":
            st.success("Recommended Career: Data Scientist")

        else:
            st.success("Recommended Career: Business Manager")

    st.markdown('</div>',unsafe_allow_html=True)

st.write("---")
st.write("JobFitBot – AI Career Advisor | Final Year Project")
