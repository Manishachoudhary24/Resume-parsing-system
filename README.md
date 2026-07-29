#  Resume Parsing System

 An AI-powered Resume Parsing System that extracts structured candidate information from PDF and DOCX resumes using a hybrid approach combining **Regular Expressions (Regex)** and **Google Gemini AI**.



## Introduction

Recruiters and HR professionals often spend significant time manually reviewing resumes to identify relevant candidate information. This project automates that process by intelligently extracting both structured and contextual information from resumes.

The system combines the accuracy of **Regular Expressions (Regex)** for extracting standard fields such as email addresses, phone numbers, LinkedIn, and GitHub profiles with the reasoning capabilities of **Google Gemini AI** to identify more complex information such as education, skills, projects, work experience, certifications, internships, and achievements.

The extracted information is merged into a structured JSON format, making it suitable for Applicant Tracking Systems (ATS), recruitment platforms, and resume analysis applications.


## Features

*  Upload resumes in **PDF** and **DOCX** formats
*  Extract text from uploaded resumes
*  Extract Email Address using Regex
*  Extract Phone Number using Regex
*  Extract LinkedIn Profile
*  Extract GitHub Profile
*  AI-powered extraction of:

  * Name
  * Address
  * Professional Summary
  * Education
  * Skills
  * Technical Skills
  * Soft Skills
  * Languages
  * Work Experience
  * Projects
  * Certifications
  * Internships
  * Achievements
*  Generate structured JSON output
*  Hybrid extraction using Regex + Large Language Model (LLM)



## System Architecture

```text
Resume (PDF/DOCX)
        │
        ▼
Document Text Extraction
        │
        ▼
Regex Extraction
(Email, Phone, LinkedIn, GitHub)
        │
        ▼
Google Gemini AI
(Contextual Information Extraction)
        │
        ▼
Merge Results
        │
        ▼
Structured JSON Output




##  Tech Stack

* Python
* Google Gemini AI API
* Regular Expressions (Regex)
* PyPDF2
* python-docx
* JSON
* Google Colab



##  Project Structure

```text
resume-parsing-system/
│
├── resume_parsing_system.ipynb
├── resume_parsing_system.py
├── requirements.txt
├── README.md
└── sample_resume.pdf (Optional)
```



##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/resume-parsing-system.git
```

### 2. Navigate to the project directory

```bash
cd resume-parsing-system
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```



## Usage

1. Open the project in **Google Colab** or run the Python script locally.
2. Add your own **Google Gemini API Key**.
3. Upload a resume in **PDF** or **DOCX** format.
4. The system extracts text from the resume.
5. Regex extracts structured fields.
6. Gemini AI extracts contextual information.
7. The extracted data is combined into a structured JSON format.



##  Sample Output

```json
{
  "Name": "John Doe",
  "Email Address": "john@example.com",
  "Phone Number": "+91-9876543210",
  "LinkedIn": "https://linkedin.com/in/johndoe",
  "GitHub": "https://github.com/johndoe",
  "Skills": [
    "Python",
    "Machine Learning",
    "SQL"
  ],
  "Education": [
    "Bachelor of Technology"
  ],
  "Projects": [
    "Resume Parsing System"
  ]
}
```



##  Applications

* Applicant Tracking Systems (ATS)
* Recruitment Automation
* Resume Screening
* HR Management Systems
* Candidate Profile Generation
* Resume Analytics



##  Future Enhancements

* Streamlit Web Interface
* Resume Ranking based on Job Description
* OCR Support for Scanned Resumes
* Multi-language Resume Parsing
* Export Results to CSV and Excel
* Batch Resume Processing
* Cloud Deployment



## Security

This repository **does not include any API keys**.

To run the project, create your own **Google Gemini API Key** and replace the placeholder in the code. Never commit or publish your actual API key.



## 📜 License

This project is licensed for educational and learning purposes.


