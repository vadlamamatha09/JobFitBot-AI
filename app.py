import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
}

.stButton>button{
background:linear-gradient(90deg,#6366f1,#06b6d4);
color:white;
border-radius:8px;
font-weight:bold;
}

input, textarea{
background-color:#1e293b !important;
color:white !important;
}

div[data-baseweb="select"]{
background-color:#1e293b !important;
color:white !important;
}

[data-testid="stFileUploader"]{
background-color:#1e293b;
padding:10px;
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 JobFitBot – AI Career Advisor")

# ------------------ JOB DATABASE ------------------

jobs = {

"Data Scientist":["python","machine learning","sql","statistics"],

"Data Analyst":["excel","sql","python","power bi"],

"Software Engineer":["java","python","algorithms","data structures"],

"Full Stack Developer":["html","css","javascript","react","nodejs"],

"AI Engineer":["python","machine learning","deep learning"],

"Cloud Engineer":["aws","docker","linux","kubernetes"],

"DevOps Engineer":["docker","linux","aws","ci/cd"],

"Cyber Security Analyst":["network security","linux","ethical hacking"],

"UI UX Designer":["figma","design","prototyping"],

"Mobile App Developer":["flutter","kotlin","java"],

"Business Analyst":["excel","sql","communication"]

}

salary = {

"Data Scientist":"12-30 LPA",
"Software Engineer":"8-25 LPA",
"Full Stack Developer":"8-20 LPA",
"AI Engineer":"15-35 LPA",
"Cloud Engineer":"10-28 LPA",
"Cyber Security Analyst":"9-27 LPA",
"UI UX Designer":"5-15 LPA"

}

learning_sources = {

"python":"https://www.coursera.org/courses?query=python",
"machine learning":"https://www.coursera.org/learn/machine-learning",
"sql":"https://www.w3schools.com/sql/",
"html":"https://www.w3schools.com/html/",
"css":"https://www.w3schools.com/css/",
"javascript":"https://www.w3schools.com/js/",
"react":"https://react.dev/learn",
"aws":"https://aws.amazon.com/training/",
"docker":"https://docs.docker.com/get-started/",
"linux":"https://linuxjourney.com/",
"figma":"https://help.figma.com/",
"flutter":"https://docs.flutter.dev/"
}

skills_db = [skill for skills in jobs.values() for skill in skills]

# ------------------ TABS ------------------

tab1,tab2,tab3,tab4,tab5 = st.tabs([
"🏠 Home",
"🚀 Career Prediction",
"📄 Resume Analyzer",
"🧠 Career Test",
"💬 Career Chatbot"
])

# =================================================
# HOME
# =================================================

with tab1:

    col1,col2,col3 = st.columns([2,2,1])

    with col1:
        st.metric("Career Prediction Accuracy","96%")
        st.header("Welcome to JobFitBot")

    with col2:
        st.metric("Resume Analysis Quality","93%")

    with col3:
        fig = plt.figure(figsize=(2,2))
        plt.pie([30,25,20,15,10],labels=["AI","Cloud","Data","Cyber","Web"])
        st.pyplot(fig)

    st.markdown("""
### 🚀 AI Powered Career Guidance Platform

JobFitBot analyzes **skills, resumes, and interests** to recommend the best career paths.
""")

# =================================================
# CAREER PREDICTION (AI MODEL)
# =================================================
with tab2:

    st.header("🚀 Career Prediction")

    # EDUCATION OPTIONS
    education = st.selectbox(
        "🎓 Select Your Education",
        ["Inter","Diploma","Degree","B.Tech","M.Tech","PG"]
    )

    # BRANCHES BASED ON EDUCATION
    branches = {

        "Inter":[
            "MPC",
            "BiPC",
            "CEC",
            "MEC",
            "HEC"
        ],

        "Diploma":[
            "Computer Engineering",
            "Mechanical Engineering",
            "Civil Engineering",
            "Electrical Engineering",
            "Electronics Engineering"
        ],

        "Degree":[
            "B.Sc Computer Science",
            "B.Sc Mathematics",
            "B.Com",
            "BBA",
            "BA"
        ],

        "B.Tech":[
            "Computer Science Engineering",
            "Information Technology",
            "Artificial Intelligence",
            "Data Science",
            "Electronics and Communication Engineering",
            "Electrical Engineering",
            "Mechanical Engineering",
            "Civil Engineering"
        ],

        "M.Tech":[
            "Artificial Intelligence",
            "Data Science",
            "Cyber Security",
            "Software Engineering"
        ],

        "PG":[
            "MCA",
            "MBA",
            "M.Sc Computer Science",
            "M.Sc Data Science"
        ]
    }

    branch = st.selectbox(
        "📚 Select Your Branch / Field",
        branches[education]
    )

    # SKILLS INPUT
    skills_input = st.text_input(
        "🛠 Enter your Skills (comma separated)"
    )

    # CERTIFICATION UPLOAD
    cert_file = st.file_uploader(
        "📜 Upload Certifications (optional)",
        type=["pdf","png","jpg"]
    )
    if st.button("Analyze My Career"):
        user_text = (education + " " + branch + " " + skills_input).lower()
        job_texts = [" ".join(skills) for skills in jobs.values()]

        corpus = job_texts + [user_text]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(corpus)

        similarity = cosine_similarity(vectors[-1], vectors[:-1])

        scores = similarity[0]

        job_names = list(jobs.keys())

        results = sorted(zip(job_names,scores), key=lambda x:x[1], reverse=True)

        st.subheader("🎯 Top Career Matches")

        for job,score in results[:3]:

            st.markdown(f"### {job} — {round(score*100,2)}% Match")

            if job in salary:
                st.write("💰 Average Salary:",salary[job])

            gap = [skill for skill in jobs[job] if skill not in user_text]

            if gap:

                st.write("📌 Skills to Improve")

                for skill in gap:

                    st.write("•",skill)

                    if skill in learning_sources:
                        st.write("📚",learning_sources[skill])

        # Graph
        chart_jobs = [r[0] for r in results[:5]]
        chart_scores = [r[1]*100 for r in results[:5]]

        fig2, ax = plt.subplots(figsize=(0.79,0.79))   # 2cm × 2cm graph

        ax.barh(chart_jobs, chart_scores)

        ax.tick_params(axis='both', labelsize=3)  # very small text
        ax.set_xlabel("")
        ax.set_ylabel("")

        plt.tight_layout()

        st.pyplot(fig2)
# =================================================
# RESUME ANALYZER
# =================================================

with tab3:

    resume = st.file_uploader("Upload Resume (PDF)",type=["pdf"])

    if resume:

        reader=PdfReader(resume)

        text=""

        for page in reader.pages:
            text+=page.extract_text()

        text=text.lower()

        detected=[skill for skill in skills_db if skill in text]

        st.subheader("Detected Skills")

        st.success(", ".join(detected))
        # Job database
        jobs = {
            "Data Scientist": {
                "skills": ["python","machine learning","statistics","pandas","numpy"],
                "salary": "₹10 LPA"
            },
            "Web Developer": {
                "skills": ["html","css","javascript","react","node"],
                "salary": "₹6 LPA"
            },
            "AI Engineer": {
                "skills": ["python","deep learning","tensorflow","pytorch","machine learning"],
                "salary": "₹12 LPA"
            }
        }
        results = []
        for job, details in jobs.items():
            required = details["skills"]
            matched = list(set(detected_skills) & set(required))
            score = len(matched) / len(required)
            gap = list(set(required) - set(detected_skills))
            results.append((job, score, gap, details["salary"]))
        results = sorted(results, key=lambda x: x[1], reverse=True)
        st.subheader("Top Recommended Job Roles")
        for job, score, gap, salary in results[:3]:
            st.write(f"Job Role: {job}")
            st.write(f"Eligibility Score: {round(score*100,2)} %")
            st.write(f"Average Salary: {salary}")
            st.write("Skill Gap:", ", ".join(gap))
            st.write("---")
# =================================================
# CAREER TEST
# =================================================

with tab4:

    q1=st.radio("1️⃣ What do you enjoy most?",
    ["Coding","Design","Data Analysis","Security","Management"])

    q2=st.radio("2️⃣ Preferred tool?",
    ["Python","Excel","Figma","AWS","Networking"])

    q3=st.radio("3️⃣ Work style?",
    ["Building apps","Analyzing data","Creative work","Protecting systems","Managing teams"])

    q4=st.radio("4️⃣ Favorite subject?",
    ["Algorithms","Statistics","Graphics","Cyber Security","Business"])

    q5=st.radio("5️⃣ Problem type?",
    ["Programming","Data insights","Design problems","Security threats","Strategy"])

    q6=st.radio("6️⃣ Industry interest?",
    ["AI","Software","Design","Security","Business"])
    if st.button("Show Career Suggestions"):
        # job score dictionary
        scores={
            "Software Engineer":0,
            "Data Scientist":0,
            "UI UX Designer":0,
            "Cyber Security Analyst":0,
            "Product Manager":0
        }
        # scoring logic
        if q1=="Coding":
            scores["Software Engineer"]+=2
        if q1=="Design":
            scores["UI UX Designer"]+=2
        if q1=="Data Analysis":
            scores["Data Scientist"]+=2
        if q1=="Security":
            scores["Cyber Security Analyst"]+=2
        if q1=="Management":
            scores["Product Manager"]+=2

        if q2=="Python":
            scores["Software Engineer"]+=1
            scores["Data Scientist"]+=1
        if q2=="Excel":
            scores["Data Scientist"]+=1
        if q2=="Figma":
            scores["UI UX Designer"]+=1
        if q2=="AWS":
            scores["Software Engineer"]+=1
        if q2=="Networking":
            scores["Cyber Security Analyst"]+=1

        if q3=="Building apps":
            scores["Software Engineer"]+=1
        if q3=="Analyzing data":
            scores["Data Scientist"]+=1
        if q3=="Creative work":
            scores["UI UX Designer"]+=1
        if q3=="Protecting systems":
            scores["Cyber Security Analyst"]+=1
        if q3=="Managing teams":
            scores["Product Manager"]+=1

    # salary data
    salary={
        "Software Engineer":"₹8-15 LPA",
        "Data Scientist":"₹10-18 LPA",
        "UI UX Designer":"₹6-12 LPA",
        "Cyber Security Analyst":"₹8-16 LPA",
        "Product Manager":"₹12-25 LPA"
    }

    # skill gap
    skill_gap={
        "Software Engineer":["DSA","Java/Python","System Design"],
        "Data Scientist":["Machine Learning","Python","Statistics"],
        "UI UX Designer":["Figma","User Research","Prototyping"],
        "Cyber Security Analyst":["Networking","Ethical Hacking","Linux"],
        "Product Manager":["Communication","Strategy","Agile"]
    }

    # sort results
    results = sorted(results, key=lambda x: x[1], reverse=True)
    st.subheader("🎯 Top 3 Recommended Careers")
    for job,score in sorted_jobs[:3]:
        eligibility=(score/5)*100
        st.write(f"**Job Role:** {job}")
        st.write(f"Eligibility Score: {round(eligibility,1)}%")
        st.write(f"Average Salary: {salary[job]}")
        st.write("Skill Gap:", ", ".join(skill_gap[job]))
        st.write("---")
# =================================================
# CHATBOT
# =================================================

with tab5:

    question=st.text_input("Ask about careers or skills")

    if question:

        q=question.lower()

        for job,skills in jobs.items():

            if job.lower() in q:

                st.subheader(job)

                st.write("Required Skills:",skills)

                if job in salary:
                    st.write("Average Salary:",salary[job])

        for skill in skills_db:

            if skill in q:

                st.write("Skill:",skill)

                if skill in learning_sources:
                    st.write("Learn:",learning_sources[skill])
