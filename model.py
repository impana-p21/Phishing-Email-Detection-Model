import joblib
import re

model = joblib.load("model.pkl")

def preprocess(text):

    urls = re.findall(r"http[s]?://\\S+", text)

    url_count = len(urls)

    cleaned = re.sub(r"http[s]?://\\S+", " URL ", text)

    return cleaned + (" URL" * url_count)

def predict_email(text):

    processed = preprocess(text)

    return model.predict([processed])[0]
