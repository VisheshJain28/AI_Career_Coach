# AI Career Coach

An AI-powered Career Coach that analyzes resumes, provides personalized feedback, answers resume-related questions, and helps candidates improve their chances of landing interviews.

Built using **Flask**, **LangChain**, **Groq LLM**, **FAISS**, and **Sentence Transformers**, the application combines Retrieval-Augmented Generation (RAG) with modern Large Language Models to deliver intelligent resume analysis.

---

# Features

- Upload Resume (PDF)
- AI-powered Resume Analysis
- Personalized Career Suggestions
- Strengths & Weakness Analysis
- Resume Improvement Recommendations
- Ask Questions About Your Resume
- Semantic Search using FAISS
- Fast Responses using Groq LLM
- Context-Aware Question Answering (RAG)

---

# Tech Stack

### Programming Language
- Python

### Backend
- Flask

### AI & LLM
- LangChain
- Groq LLM

### Vector Database
- FAISS

### Embeddings
- Sentence Transformers

### PDF Processing
- PyPDF2

### Machine Learning
- HuggingFace Transformers

### Others

- HTML
- CSS
- Jinja2
- Gunicorn

---

# Project Architecture

```
                User
                  │
                  ▼
          Upload Resume (PDF)
                  │
                  ▼
          PDF Text Extraction
                  │
                  ▼
         Text Chunking Process
                  │
                  ▼
 Sentence Transformer Embeddings
                  │
                  ▼
        FAISS Vector Database
                  │
                  ▼
      Retrieval-Augmented Generation
                  │
                  ▼
             Groq LLM
          ┌───────────────┐
          │               │
          ▼               ▼
 Resume Analysis     Resume Q&A
          │               │
          └──────┬────────┘
                 ▼
          AI Generated Output
```

---

# Project Structure

```
AI_Career_Coach/

│── app.py
│── config.py
│── requirements.txt
│── templates/
│── uploads/
│── src/
│   ├── llm.py
│   ├── prompts.py
│   ├── qa.py
│   ├── vector_store.py
│   ├── pdf_loader.py
│
└── vector_index/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/VisheshJain28/AI_Career_Coach.git
```

Move into the project

```bash
cd AI_Career_Coach
```

Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Mac/Linux

```bash
python3 -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file

```
GROQ_API_KEY=YOUR_API_KEY
```

---

# Run Project

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Workflow

1. Upload Resume
2. Extract Text
3. Split into Chunks
4. Generate Embeddings
5. Store Embeddings in FAISS
6. Retrieve Relevant Context
7. Generate AI Response using Groq
8. Display Resume Analysis
9. Ask Questions about Resume

---

# Key Features Explained

### Resume Analysis

The uploaded resume is analysed using a Large Language Model to generate personalized feedback on content, skills, strengths, weaknesses and improvement areas.

### Resume Question Answering

Users can ask questions like

- What are my strengths?
- Which skills are missing?
- How can I improve my resume?
- Is my resume ATS friendly?

The system retrieves relevant resume sections using FAISS before sending context to the LLM.

---

# Future Improvements

- ATS Score Generation
- Resume Keyword Matching
- Job Recommendation System
- Cover Letter Generator
- Interview Preparation Module
- Resume Version Comparison
- Multi-language Resume Support
- Dashboard Analytics
- User Authentication

---

# Why This Project?

Recruiters spend only a few seconds reviewing resumes.

This project leverages Retrieval-Augmented Generation (RAG) and Large Language Models to automate resume evaluation, generate actionable insights, and provide interactive question answering, helping users build stronger resumes and prepare for interviews.

---

# Tech Concepts Used

- Generative AI
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Prompt Engineering
- Vector Embeddings
- Large Language Models
- PDF Parsing
- FAISS Indexing
- Document Chunking
