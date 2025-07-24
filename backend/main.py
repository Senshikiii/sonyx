from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize FastAPI app
app = FastAPI()

# Strong, multi-origin CORS setup
origins = [
    "http://localhost:3000",      # React/Vite/etc
    "http://127.0.0.1:3000",
    "http://localhost:8000",      # backend (optional)
    "http://127.0.0.1:8000",
    "http://localhost",           # local file:// fallback
    "*"                           # wildcard fallback (not recommended in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # use ["*"] in dev, restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and vectorizer
MODEL_PATH = "../ml_model/vuln_classifier_model.pkl"
VECTORIZER_PATH = "../ml_model/tfidf_vectorizer.pkl"

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as load_err:
    print(f"❌ Failed to load model or vectorizer: {load_err}")
    model = None
    vectorizer = None

# Define input schema
class CodeInput(BaseModel):
    code: str

# Define prediction route
@app.post("/predict")
def predict(input: CodeInput):
    if model is None or vectorizer is None:
        return {"error": "Model not loaded"}

    try:
        code = input.code
        code_vector = vectorizer.transform([code])
        prediction = model.predict(code_vector)[0]
        return {"vulnerability": prediction}
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}
    

