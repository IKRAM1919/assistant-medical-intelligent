
from pydantic import BaseModel

class PatientData(BaseModel):
    age: float
    bp: float
    glucose: float
    bmi: float
    cholesterol: float
    creatinine: float
    hemoglobin: float
    heart_rate: float
    hypertension: int
    diabetes_history: int
    anemia: int
