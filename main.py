import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
from bs4 import BeautifulSoup
import opendatasets as od

dataset_url = "https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=phishing_email.csv"
download_path = "./phishing_email_dataset"
if not os.path.exists(download_path):
    od.download(dataset_url, data_dir=download_path)

csv_path = os.path.join(download_path, "phishing-email-dataset", "phishing_email.csv")
df = pd.read_csv(csv_path)
# print("CSV loaded. Rows")

df.drop_duplicates(inplace=True)
print("Dropped duplicates")

# Preprocessing function
def preprocess_text(text, unwanted_terms):
    text = text.lower()
    text = re.sub(r'\b\w*\d\w*\b', '', text)  # remove words with numbers
    text = BeautifulSoup(text, 'html.parser').get_text()  # strip HTML
    text = re.sub(r'\b(?:mon|tue|wed|thu|fri|sat|sun)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b', '', text, flags=re.IGNORECASE)
    for term in unwanted_terms:
        text = re.sub(rf'\b{re.escape(term)}\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    text = re.sub(r'\b_+\b', '', text)  # remove underscore-only words
    return text

# Apply preprocessing
unwanted_terms = ['enron', 'hpl', 'nom', 'forwarded', '2008', '10', 'hplno', 'xls']
df['text_combined'] = df['text_combined'].astype(str).apply(lambda x: preprocess_text(x, unwanted_terms))
print("Preprocessing complete.")

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text_combined'])
y = df['label']
print("Vectorization complete.")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Split complete.")

# Train SVM
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
print("Model trained.")

# Evaluate
accuracy = svm_model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

import joblib

# Save the model
joblib.dump(svm_model, "svm_model.pkl")
print("SVM model saved to 'svm_model.pkl'")

# Save the vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("TF-IDF vectorizer saved to 'tfidf_vectorizer.pkl'")
