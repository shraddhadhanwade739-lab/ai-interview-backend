import os
from fastapi import FastAPI, UploadFile, File, Form
from app.supabase_client import supabase, upload_file

app = FastAPI()

# ✅ Root endpoint to confirm backend is running
@app.get("/")
async def root():
    return {"message": "Backend is running!"}

@app.post("/upload/interview")
async def upload_interview(
    resume: UploadFile = File(...),
    recording: UploadFile = File(...),
    score: float = Form(...),
    report: str = Form(...)
):
    # Save files temporarily
    resume_path = f"temp_{resume.filename}"
    recording_path = f"temp_{recording.filename}"

    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    with open(recording_path, "wb") as f:
        f.write(await recording.read())

    # Upload to Supabase Storage
    resume_url = upload_file("resumes", resume_path)
    recording_url = upload_file("recordings", recording_path)

    # Clean up local temp files
    os.remove(resume_path)
    os.remove(recording_path)

    # Insert into interview_analysis table
    data = {
        "resume_url": resume_url,
        "recording_url": recording_url,
        "score": score,
        "report": report,
    }

    result = supabase.table("interview_analysis").insert(data).execute()

    return {
        "message": "Interview data uploaded successfully",
        "resume_url": resume_url,
        "recording_url": recording_url,
        "db_result": result.data
    }
