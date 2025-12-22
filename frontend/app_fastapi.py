from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

with open("../student_score_model.pkl", "rb") as f:

    model = pickle.load(f)

class StudentInput(BaseModel):
    hours_studied: float
    sleep_hours: float
    attendance_percent: float
    previous_scores: float

@app.post("/predict")
def predict(data: StudentInput):
    X = np.array([[ 
        data.hours_studied,
        data.sleep_hours,
        data.attendance_percent,
        data.previous_scores
    ]])
    y = model.predict(X)
    return {"predicted_exam_score": float(y[0])}
