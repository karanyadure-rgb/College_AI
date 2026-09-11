# TSSM AI

AI-powered learning assistant for Diploma Computer Engineering students.

TSSM AI provides students with simple explanations, exam-ready answers, and study-material summarization using Google Gemini.

## 🚀 Features

### 🤖 AI Tutor

Ask technical and academic questions and receive clear, student-friendly explanations.

### 📚 Unit Explanation

Provide a subject, unit, and syllabus topics to generate a complete, structured, and exam-oriented explanation.

### ✍️ Exam Answer Generator

Generate exam-ready answers according to MSBTE-style marks:

- 2 Marks
- 4 Marks
- 6 Marks

### 📝 Summarizer

Summarize study material into easy-to-revise notes.

Supported inputs:

- Pasted text
- PDF
- DOCX

Summary options:

- Short
- Medium
- Detailed

## 🛠️ Technology Stack

### Backend

- Python
- Flask
- Google Gemini
- google-genai
- python-dotenv

### Document Processing

- pypdf
- python-docx

### Testing Interface

- Streamlit
- Requests

## 📁 Project Structure

```text
tssm-ai/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── gemini.py
│   │
│   ├── tutor/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── service.py
│   │
│   ├── unit_explanation/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── service.py
│   │
│   ├── exam_answer/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── service.py
│   │
│   └── summarization/
│       ├── __init__.py
│       ├── router.py
│       ├── service.py
│       └── extractor.py
│
├── streamlit_app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
