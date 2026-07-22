import joblib

model=joblib.load("model.pkl")

def predict_email(text):
    return model.predict([text])[0]
