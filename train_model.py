import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

data=pd.read_csv("dataset.csv")

model=Pipeline([
("tfidf",TfidfVectorizer()),
("clf",LogisticRegression())
])

model.fit(data["text"],data["label"])

joblib.dump(model,"model.pkl")

print("Model Trained Successfully")
