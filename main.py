from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pandas as pd
import joblib

app = FastAPI()

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Load Model
model = joblib.load("model/placement_model.pkl")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": None,
            "probability": None
        }
    )


@app.post("/", response_class=HTMLResponse)
async def predict(
    request: Request,

    age: int = Form(...),
    gender: str = Form(...),
    cgpa: float = Form(...),
    branch: str = Form(...),
    college_tier: str = Form(...),

    internships_count: int = Form(...),
    projects_count: int = Form(...),
    certifications_count: int = Form(...),

    coding_skill_score: int = Form(...),
    aptitude_score: int = Form(...),
    communication_skill_score: int = Form(...),
    logical_reasoning_score: int = Form(...),

    hackathons_participated: int = Form(...),
    github_repos: int = Form(...),
    linkedin_connections: int = Form(...),

    mock_interview_score: int = Form(...),
    attendance_percentage: float = Form(...),

    backlogs: int = Form(...),

    extracurricular_score: int = Form(...),
    leadership_score: int = Form(...),

    volunteer_experience: str = Form(...),

    sleep_hours: float = Form(...),
    study_hours_per_day: float = Form(...)
):

    data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "cgpa": cgpa,
        "branch": branch,
        "college_tier": college_tier,
        "internships_count": internships_count,
        "projects_count": projects_count,
        "certifications_count": certifications_count,
        "coding_skill_score": coding_skill_score,
        "aptitude_score": aptitude_score,
        "communication_skill_score": communication_skill_score,
        "logical_reasoning_score": logical_reasoning_score,
        "hackathons_participated": hackathons_participated,
        "github_repos": github_repos,
        "linkedin_connections": linkedin_connections,
        "mock_interview_score": mock_interview_score,
        "attendance_percentage": attendance_percentage,
        "backlogs": backlogs,
        "extracurricular_score": extracurricular_score,
        "leadership_score": leadership_score,
        "volunteer_experience": volunteer_experience,
        "sleep_hours": sleep_hours,
        "study_hours_per_day": study_hours_per_day
    }])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    result = "Highly Likely To Get Placed ✅🚀" if prediction == 1 else "Not Placed ❌ Needs Improvement 📚"
    

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": result,
            "probability": round(probability * 100, 2)
        }
    )