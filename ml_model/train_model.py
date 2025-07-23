import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# 1. Load the CSV data
csv_path = "../data/processed_contracts/labeled_data.csv"
df = pd.read_csv(csv_path)

# 2. Extract features and labels
X_raw = df["code"]
y = df["label"]

# 3. Convert code to numeric features
vectorizer = TfidfVectorizer(max_features=3000)  # limit for speed
X = vectorizer.fit_transform(X_raw)

# 4. Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train a classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

# 7. Save the model + vectorizer
joblib.dump(model, "vuln_classifier_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model and vectorizer saved in ml_model/")