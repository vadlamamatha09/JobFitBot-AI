import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

st.set_page_config(page_title="JobFitBot", layout="wide")

# ---------- BACKGROUND ----------

st.markdown(
"""
<style>

.stApp{
background-image:url("https://images.unsplash.com/photo-1581094794329-c8112a89af12");
background-size:cover;
background-attachment:fixed;
}

.box{
background:rgba(255,255,255,0.93);
padding:25px;
border-radius:12px;
}

</style>
""",
unsafe_allow_html=True
)

# ---------- TITLE ----------

st.title("🤖 JobFitBot – AI Career Advisor")

# ---------- TABS ----------

tab1, tab2, tab3, tab4 = st.tabs(
["🏠 Home","📄 Resume Analyzer","🚀 Career Prediction","🧠 Career Test"]
)

# =========================================================
# HOME TAB
# =========================================================

with tab1:

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.header("Welcome to JobFitBot")

    st.write(
    """
    JobFitBot is an AI based career guidance platform that helps students:

    ✔ Discover the best career path  
    ✔ Analyze skills and certifications  
    ✔ Understand job readiness  
    ✔ Get career improvement suggestions
    """
    )

    st.subheader("How It Works")

    st.write(
    """
    1️⃣ Upload your resume  
    2️⃣ Enter your skills or certifications  
    3️⃣ Click career prediction  
    4️⃣ Get best career matches instantly
    """
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RESUME ANALYZER TAB
# =========================================================

with tab2:

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.header("📄 Resume Analyzer")

    resume_file = st.file_uploader("Upload Resume (PDF)")

    skill_database = [
    "python","java","machine learning","sql",
    "html","css","javascript","react",
    "aws","docker","linux","excel"
    ]

    resume_skills = []

    if resume_file:

        reader = PdfReader(resume_file)

        text=""

        for page in reader.pages:
            text+=page.extract_text()

        text=text.lower()

        for skill in skill_database:
            if skill in text:
                resume_skills.append(skill)

        st.success("Skills detected from resume")

        st.write(resume_skills)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CAREER PREDICTION TAB
# =========================================================

with tab3:

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.header("🚀 Career Prediction")

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

    # ---------- SIDE CHARTS ----------

    col1,col2=st.columns([3,1])

    with col2:

        st.subheader("Skill Chart")

        if skills_input:

            skills=[i.strip() for i in skills_input.split(",")]

            fig=plt.figure(figsize=(2,2))
            plt.pie([1]*len(skills),labels=skills)

            st.pyplot(fig)

        st.subheader("Tech Trends")

        labels=["AI","Cloud","Cyber","Data"]
        sizes=[30,25,25,20]

        fig2=plt.figure(figsize=(2,2))
        plt.pie(sizes,labels=labels)

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

    # ---------- ANALYZE ----------

    if st.button("Analyze My Career"):

        if skills_input=="":

            st.warning("Please enter skills")

        else:

            user_skills=[i.strip().lower() for i in skills_input.split(",")]

            results=[]

            for job,req in jobs.items():

                matched=len(set(user_skills)&set(req))
                score=(matched/len(req))*100
                gap=list(set(req)-set(user_skills))

                results.append((job,score,gap))

            results=sorted(results,key=lambda x:x[1],reverse=True)

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

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CAREER TEST TAB
# =========================================================

with tab4:

    st.markdown('<div class="box">', unsafe_allow_html=True)

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

    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.write("JobFitBot – AI Career Advisor | Final Year Project")
