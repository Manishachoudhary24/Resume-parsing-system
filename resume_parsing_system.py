# -*- coding: utf-8 -*-




## Resume Parsing system
"""

import google.generativeai as genai

# Using the provided API key
GOOGLE_API_KEY = "Enter you API KEY here"
genai.configure(api_key=GOOGLE_API_KEY)

print("Gemini API configured successfully!")

try:
    # Using 'gemini-flash-latest' which is available in this environment
    llm_model = genai.GenerativeModel('gemini-flash-latest')
    print("Gemini Flash (Latest) initialized successfully.")
except Exception as e:
    print(f"Error initializing model: {e}")
    llm_model = None

"""### 2. Resume Upload and Text Extraction


"""

# Install necessary libraries if not already installed
!pip install PyPDF2 python-docx

import io
import re
from google.colab import files
import PyPDF2
import docx

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def extract_text_from_docx(docx_file):
    """Extracts text from a DOCX file."""
    text = ""
    try:
        document = docx.Document(docx_file)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text

# Main function to handle file upload and extraction
def upload_and_extract_text():
    uploaded = files.upload()
    for filename, content in uploaded.items():
        file_extension = filename.split('.')[-1].lower()
        if file_extension == 'pdf':
            print(f"Processing PDF file: {filename}")
            return extract_text_from_pdf(io.BytesIO(content)), filename
        elif file_extension == 'docx':
            print(f"Processing DOCX file: {filename}")
            return extract_text_from_docx(io.BytesIO(content)), filename
        else:
            print(f"Unsupported file type: {filename}. Please upload a PDF or DOCX.")
            return None, None

print("Please upload your resume (PDF or DOCX format):")
resume_text, uploaded_filename = upload_and_extract_text()

if resume_text:
    print(f"Successfully extracted text from {uploaded_filename}. First 500 characters:\n{resume_text[:500]}...")
else:
    print("No text extracted. Please try uploading a valid resume file.")

"""### 3. Regex-based Extraction for Structured Fields

"""

def extract_with_regex(text):
    """Extracts structured information using regex."""
    extracted_data = {}

    # Email Address
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    if emails: extracted_data['email'] = list(set(emails)) # Use set to remove duplicates

    # Phone Number (more flexible pattern)
    phone_pattern = r'\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}' # Matches (123) 456-7890, 123-456-7890, 123 456 7890, 123.456.7890
    phones = re.findall(phone_pattern, text)
    if phones: extracted_data['phone_number'] = list(set(phones))

    # LinkedIn Profile
    linkedin_pattern = r'linkedin\.com/in/[a-zA-Z0-9_-]+'
    linkedins = re.findall(linkedin_pattern, text)
    if linkedins: extracted_data['linkedin_profile'] = [f"https://{url}" for url in list(set(linkedins))]

    # GitHub Profile
    github_pattern = r'github\.com/[a-zA-Z0-9_-]+'
    githubs = re.findall(github_pattern, text)
    if githubs: extracted_data['github_profile'] = [f"https://{url}" for url in list(set(githubs))]

    return extracted_data

if resume_text:
    regex_extracted_info = extract_with_regex(resume_text)
    print("Regex-based Extraction Results:")
    print(regex_extracted_info)
else:
    regex_extracted_info = {}
    print("Cannot perform regex extraction: No resume text available.")

""" 4. LLM-based Extraction for Contextual Information


"""

import json

def get_llm_extraction_prompt(resume_content):
    """Generates the prompt for the LLM to extract resume information."""
    prompt = f"""You are an expert resume parser. Extract information from the provided resume text and format it as a JSON object.

Strictly include these keys in the output:
- Name
- Phone Number
- Email Address
- Address
- LinkedIn
- GitHub
- Professional Summary (Objective)
- Education
- Skills
- Technical Skills
- Soft Skills
- Languages
- Work Experience
- Projects
- Certifications
- Internships
- Achievements

Return ONLY the raw JSON object. Do not include markdown code fences or extra text.

Resume Text:
{resume_content}
"""
    return prompt

import json

if resume_text and llm_model:
    print("Sending resume text to Gemini for advanced extraction...")
    llm_prompt = get_llm_extraction_prompt(resume_text)

    try:
        # Generate content
        response = llm_model.generate_content(llm_prompt)

        if response and response.text:
            llm_output_text = response.text.strip()

            # Clean JSON markdown fences if the model includes them
            if "```" in llm_output_text:
                if "```json" in llm_output_text:
                    llm_output_text = llm_output_text.split("```json")[1].split("```")[0].strip()
                else:
                    llm_output_text = llm_output_text.split("```")[1].split("```")[0].strip()

            llm_extracted_info = json.loads(llm_output_text)
            print("LLM-based Extraction Results (Success!)")
            display(llm_extracted_info)
        else:
            print("No text returned from Gemini.")
            llm_extracted_info = {}
    except Exception as e:
        print(f"Extraction failed: {e}")
        llm_extracted_info = {}
else:
    print("Missing resume text or model initialization.")
    llm_extracted_info = {}

""" 5. Combine and Display Final Output


"""

import json

# 1. Start with the comprehensive LLM data
final_parsed_resume = {}
if 'llm_extracted_info' in locals() and llm_extracted_info:
    final_parsed_resume = llm_extracted_info.copy()

# 2. Use Regex results to ensure deterministic fields are accurate
# Regex is often more precise for standard patterns like emails and phone numbers
if 'regex_extracted_info' in locals() and regex_extracted_info:
    if 'email' in regex_extracted_info:
        final_parsed_resume['Email Address'] = regex_extracted_info['email'][0]
    if 'phone_number' in regex_extracted_info:
        final_parsed_resume['Phone Number'] = regex_extracted_info['phone_number'][0]
    if 'linkedin_profile' in regex_extracted_info:
        final_parsed_resume['LinkedIn'] = regex_extracted_info['linkedin_profile'][0]
    if 'github_profile' in regex_extracted_info:
        final_parsed_resume['GitHub'] = regex_extracted_info['github_profile'][0]

# Display the final structured result
print("\n--- Final Parsed Resume (JSON) ---")
print(json.dumps(final_parsed_resume, indent=2))