import streamlit as st

st.set_page_config(page_title="JobFitBot", layout="wide")

st.title("🤖 JobFitBot – AI Career Advisor")

st.write("Find the best job roles based on your skills")

skills_input = st.text_input("Enter your skills (comma separated)")

jobs = {
    "Data Scientist":["python","machine learning","statistics","sql"],
    "Web Developer":["html","css","javascript","react"],
    "Software Engineer":["python","java","data structures","algorithms"],
    "AI Engineer":["python","deep learning","tensorflow","nlp"],
    "Data Analyst":["excel","sql","python","powerbi"]
}

if st.button("Analyze Career"):
    
    user_skills = [i.strip().lower() for i in skills_input.split(",")]
    
    results = []
    
    for job,req in jobs.items():
        
        matched = len(set(user_skills) & set(req))
        score = matched/len(req)*100
        
        results.append((job,score))
    
    results = sorted(results,key=lambda x:x[1],reverse=True)
    
    for job,score in results:
        
        st.subheader(job)
        st.progress(int(score))
        st.write(f"Match Score: {score:.2f}%")
