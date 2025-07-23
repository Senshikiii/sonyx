from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can set this to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model + vectorizer
MODEL_PATH = "../ml_model/vuln_classifier_model.pkl"
VECTORIZER_PATH = "../ml_model/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

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
    


    