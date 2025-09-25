# 🤖 AI-Powered Resume Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google AI](https://img.shields.io/badge/Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

An intelligent tool built to analyze your resume against a job description, providing both a quantitative match score and qualitative, AI-driven feedback for improvement.

---

## 📖 About The Project

In a competitive job market, tailoring a resume for each application is critical but time-consuming. This tool streamlines that process by offering instant, comprehensive analysis. It helps job seekers quickly identify keyword gaps and understand how to better align their resume with a potential employer's needs, increasing their chances of passing automated screening systems and catching a recruiter's eye.



---

## ✨ Key Features

* **📄 Resume Parsing:** Supports both `PDF` and `DOCX` file formats for easy uploading.
* **📊 Keyword Analysis:** Calculates a percentage match score by comparing keywords from the job description against the resume content.
* **✅ Matched & ❌ Missing Keywords:** Clearly lists which critical keywords are present and which are missing.
* **🧠 AI-Powered Feedback:** Integrates **Google's Gemini AI** to provide qualitative feedback like a career coach, including a summary, a list of strengths, and actionable suggestions.

---

## 🛠️ Tech Stack

| Category         | Technology                                             |
| ---------------- | ------------------------------------------------------ |
| **Language** | Python 3.9+                                            |
| **Web Framework**| Streamlit                                              |
| **NLP/Analysis** | NLTK (Natural Language Toolkit)                        |
| **AI Integration**| Google Generative AI (Gemini 1.5 Flash)                |
| **File Parsing** | PyPDF2, python-docx                                    |

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.9 or higher
* A Google Gemini API Key. You can get one for free from **[Google AI Studio](https://aistudio.google.com/app/apikey)**.

### Local Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your local API Key:**
    * Create a folder in your project directory named `.streamlit`.
    * Inside the `.streamlit` folder, create a file named `secrets.toml`.
    * Add your Google Gemini API key to the `secrets.toml` file like this:
        ```toml
        GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
        ```

5.  **Run the application:**
    ```sh
    streamlit run app.py
    ```

---

## 📝 How to Use

1.  **Upload Resume:** Select your resume in PDF or DOCX format.
2.  **Paste Job Description:** Paste the full text of a job description into the text area.
3.  **Analyze:** Click the "Analyze Your Resume" button.
4.  **Review Results:** View your keyword match score and read the AI-powered feedback to see how you can improve your resume.
