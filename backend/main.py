from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Load your trained model + vectorizer
MODEL_PATH = "../ml_model/vuln_classifier_model.pkl"
VECTORIZER_PATH = "../ml_model/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Define input schema
class CodeInput(BaseModel):
    code: str

@app.post("/predict")
def predict(input: CodeInput):
    try:
        code = input.code
        code_vector = vectorizer.transform([code])
        prediction = model.predict(code_vector)[0]
        return {"vulnerability": prediction}
    except Exception as e:
        return {"error": str(e)}
    




