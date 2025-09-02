Resume Q&A with FastAPI


A FastAPI-powered application that lets you upload your resume and ask natural language questions about it.
It extracts text from your resume and provides context-aware answers instantly.

🚀 Features

📂 Upload your resume (.txt format)

❓ Ask questions about your resume

🤖 Get instant, context-based answers

🌐 Interactive API docs at /docs

🛠️ Tech Stack

Python 3.9+

FastAPI (backend framework)

Uvicorn (ASGI server)

📂 Project Structure
resume-qa-app/
│── app.py              # Main FastAPI app
│── requirements.txt    # Dependencies
│── resume.txt          # Sample resume file
│── README.md           # Documentation

▶️ Run Locally

Clone this repository

git clone https://github.com/AncyJudilK/resume-qa-llm.git



Create a virtual environment

python -m venv venv
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Start the app

uvicorn app:app --reload --port 8000


Open in browser
👉 http://127.0.0.1:8000/docs

☁️ Deploy on Render

Push your repo to GitHub

Go to Render
 → New Web Service → Connect your repo

Add:

Build Command: pip install -r requirements.txt

Start Command: ./start.sh

Deploy 🚀

📖 API Endpoints
🔹 Upload Resume
POST /upload_resume/


Body: resume file (txt format)

🔹 Ask Question
POST /ask_question/


JSON body:

{
  "question": "What is my experience?"
}


✅ Example Response:

{
  "answer": "You have 2 years of experience in Python, FastAPI, and Machine Learning."
}

