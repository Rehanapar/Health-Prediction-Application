import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def predict_health(glucose, haemoglobin, cholesterol):
    prompt = f"""
        You are a medical AI assistant.

        A patient has the following blood test values:

        Glucose: {glucose}
        Haemoglobin: {haemoglobin}
        Cholesterol: {cholesterol}

        Predict the patient's health condition.

        Return ONLY ONE of these exactly:

        Healthy
        Pre-Diabetes
        High Diabetes Risk
        Possible Anemia
        High Cholesterol Risk

        Do not explain your answer.
        Do not return any extra text.
        """

    payload = {
        "model": "openai/gpt-4.1-nano",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        prediction = (
            result["choices"][0]["message"]["content"]
            .strip()
            .replace("\n", "")
        )

        return prediction

    except Exception as e:
        print("Prediction Error:", str(e))

        if 'response' in locals():
            print("Response:", response.text)

        return "Prediction Failed"