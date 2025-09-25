# -----------------------------------------
import streamlit as st
import docx
import PyPDF2
import nltk
import io
import os
import google.generativeai as genai

# This MUST be the only NLTK setup code at the top of your file
nltk_data_dir = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_dir)
# Configure the Gemini API key from Streamlit secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("Error configuring the Google API. Please ensure your API key is correctly set in .streamlit/secrets.toml")

# --- Core Functions (The "Backend") ---

def extract_text_from_docx(file_like_object):
    doc = docx.Document(file_like_object)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def extract_text_from_pdf(file_like_object):
    pdf_reader = PyPDF2.PdfReader(file_like_object)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def extract_keywords(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = nltk.tokenize.word_tokenize(text.lower())
    keywords = [word for word in words if word.isalpha() and word not in stop_words]
    return set(keywords)

def analyze_resume(resume_text, jd_keywords):
    resume_text_lower = resume_text.lower()
    matched_keywords = [keyword for keyword in jd_keywords if keyword in resume_text_lower]
    missing_keywords = [keyword for keyword in jd_keywords if keyword not in resume_text_lower]
    score = (len(matched_keywords) / len(jd_keywords)) * 100 if jd_keywords else 0
    return matched_keywords, missing_keywords, score

def get_gemini_feedback(resume_text, jd_text):
    prompt = f"""
    You are an expert career coach and resume analyst.
    Analyze the following resume and job description and provide constructive feedback.
    **Resume Text:** {resume_text}
    **Job Description Text:** {jd_text}
    **Instructions:** Provide your analysis in Markdown format with sections for: '1. Overall Summary', '2. Strengths', '3. Actionable Suggestions for Improvement', and '4. Missing Keywords Analysis'.
    """
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating AI feedback: {str(e)}"

# --- Streamlit UI (The "Frontend") ---
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖", layout="wide")
st.title("🤖 AI-Powered Resume Analyzer")
st.markdown("Get instant feedback on your resume! This tool analyzes your resume against a job description to give you a match score and AI-driven suggestions for improvement.")
st.divider()

col1, col2 = st.columns([1, 2])
with col1:
    st.header("Your Resume")
    uploaded_resume = st.file_uploader("Upload your resume file (PDF or DOCX)", type=['pdf', 'docx'], label_visibility="collapsed")
    enable_ai_feedback = st.checkbox("Enable AI-Powered Feedback", value=True)
with col2:
    st.header("The Job Description")
    job_description = st.text_area("Paste the job description here", height=350, label_visibility="collapsed")

if st.button("Analyze Your Resume", type="primary", use_container_width=True):
    if uploaded_resume is not None and job_description:
        with st.spinner('Analyzing... This may take a moment.'):
            resume_text = ""
            if uploaded_resume.type == "application/pdf":
                resume_text = extract_text_from_pdf(io.BytesIO(uploaded_resume.getvalue()))
            else:
                resume_text = extract_text_from_docx(io.BytesIO(uploaded_resume.getvalue()))
            
            jd_keywords = extract_keywords(job_description)
            matched, missing, score = analyze_resume(resume_text, jd_keywords)
            
            st.divider()
            st.header("Keyword Analysis")
            st.subheader(f"Keyword Match Score: {score:.2f}%")
            st.progress(int(score))
            
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                with st.expander(f"✅ Matched Keywords ({len(matched)})", expanded=True):
                    st.write(", ".join(sorted(matched)) or "No keywords matched.")
            with res_col2:
                with st.expander(f"❌ Missing Keywords ({len(missing)})", expanded=True):
                    st.write(", ".join(sorted(missing)) or "Great job! No critical keywords are missing.")
            
            if enable_ai_feedback:
                st.divider()
                st.header("🤖 AI-Powered Smart Feedback")
                with st.spinner("Our AI Coach is analyzing your resume..."):
                    ai_feedback = get_gemini_feedback(resume_text, job_description)
                    st.markdown(ai_feedback)
    else:
        st.error("Please upload your resume and paste the job description.")