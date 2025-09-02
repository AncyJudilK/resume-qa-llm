from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


try:
    with open("data/resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
except FileNotFoundError:
    resume_text = ""

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Resume Q&A API is running!"}

@app.post("/query")
def query_resume(request: QueryRequest):
    if not resume_text:
        raise HTTPException(status_code=500, detail="Resume file not found or empty.")

    query = request.query.lower()

    if "skills" in query:
        return {"answer": "Ancy's skills include Python, AI/ML, OCR, Generative AI, and job scraping."}
    elif "projects" in query:
        return {"answer": "Ancy has worked on OCR, AI Voice Assistant, Fraud Detection ML, Job Scraping, and Generative AI."}
    elif "experience" in query:
        return {"answer": "Ancy has 1.5 years of experience in AI/ML development."}
    else:
        return {"answer": "Sorry, I couldn't find information about that in the resume."}
