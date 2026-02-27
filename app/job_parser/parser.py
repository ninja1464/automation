from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.job_parser.parser import parse_job
from app.matcher.scoring import score_job
from app.resume_generator.generator import generate_resume

app = FastAPI()

class JobInput(BaseModel):
    job_text: str

@app.post("/analyze")
async def analyze_job(data: JobInput):
    parsed = parse_job(data.job_text)
    score = score_job(parsed)

    return {
        "parsed_job": parsed,
        "match_score": round(score, 3)
    }

@app.post("/generate_resume")
async def create_resume(data: JobInput):
    resume_path = generate_resume(data.job_text)
    return {"resume_file": resume_path}