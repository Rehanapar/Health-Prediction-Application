import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "ml", "health_model.pkl")
)

def predict_health(glucose, haemoglobin, cholesterol):
    prediction = model.predict([[glucose, haemoglobin, cholesterol]])
    return prediction[0]