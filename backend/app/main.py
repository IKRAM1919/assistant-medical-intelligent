
from fastapi import FastAPI
from app.schemas import PatientData
from app.model import predict_disease
from app.llm_chat import explain_diagnosis

app = FastAPI(title="Assistant Médical Intelligent")

@app.post("/diagnose")
def diagnose(patient: PatientData):
    patient_dict = patient.dict()
    disease = predict_disease(patient_dict)
    explanation = explain_diagnosis(disease, patient_dict)
    return {"predicted_disease": disease, "explanation": explanation}

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'Assistant Médical Intelligent"}
