
import pandas as pd
import joblib

# Charger modèle et label encoder
model = joblib.load("models/best_medical_diagnosis_model.pkl")
le = joblib.load("models/label_encoder.pkl")

features = ['age', 'bp', 'glucose', 'bmi', 'cholesterol', 'creatinine',
            'hemoglobin', 'heart_rate', 'hypertension', 'diabetes_history', 'anemia']

def predict_disease(patient_data: dict):
    df = pd.DataFrame([patient_data])
    df = df[features]
    pred = model.predict(df)[0]
    disease = le.inverse_transform([pred])[0]
    return disease
