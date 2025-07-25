🔍 Sonyx — AI Smart Contract Auditor

Live Demo: https://sonyx-nu.vercel.appBackend API: https://sonyx-3.onrender.com

Sonyx is an open-source AI-powered smart contract auditor built in 72 hours for a hackathon. It scans Solidity contracts and predicts potential vulnerabilities using a trained machine learning model.

🧠 Key Features

Detects common Solidity vulnerabilities:

Reentrancy

Integer Overflow

Timestamp Dependence

Access Control

Unchecked External Calls

Frontend built from scratch

FastAPI backend with ML inference

Trained custom model using TF-IDF + Scikit-learn

Fully deployed frontend + backend

🚀 Tech Stack

Layer

Technology

Frontend

Vanilla HTML + JS

Backend

FastAPI

ML Model

Scikit-learn, TF-IDF, Joblib

Hosting

Vercel (frontend), Render (API)

Tools

Git, GitHub

📚 How It Works

User pastes Solidity code in the UI

Backend receives the code at /predict

The ML model classifies vulnerability type

UI displays severity + recommendations

🚧 Local Setup

Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Make sure your model files are in place:

../ml_model/vuln_classifier_model.pkl

../ml_model/tfidf_vectorizer.pkl

Frontend

You can open index.html directly or deploy via Vercel.

🧰 API Usage

POST /predict

Request Body:

{
  "code": "pragma solidity ^0.8.0; contract X { ... }"
}

Response:

{
  "vulnerability": "REENTRANCY"
}

🌟 What I Learned

Training and saving ML models

Connecting ML to APIs via FastAPI

Building and styling frontend apps

Deployment on Vercel and Render

End-to-end shipping of a product

Commits in production = real founder behavior

🚀 Future Plans

Rebuild frontend in React + Tailwind

Add dark mode and better UX

Improve model accuracy + show confidence score

Add multiple vulnerability detection



📄 License

MIT License. Fork it, use it, remix it.

🙏 Credits

Built by @Senshikiii — powered by AI, shipped with intent.

"It doesn't matter if you're committing to production — what matters is you're committing to ship."

