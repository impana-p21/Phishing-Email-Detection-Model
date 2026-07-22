import pandas as pd
import joblib
import re

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv("dataset.csv")

def preprocess(text):

    urls = re.findall(r"http[s]?://\\S+", text)

    url_count = len(urls)

    cleaned = re.sub(r"http[s]?://\\S+", " URL ", text)

    return cleaned + (" URL" * url_count)

data["processed"] = data["text"].apply(preprocess)

X = data["processed"]

y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

cm = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)

print("Confusion Matrix")

print(cm)

joblib.dump(model, "model.pkl")
