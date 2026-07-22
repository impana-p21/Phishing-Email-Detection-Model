from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Phishing Email Detection Model"

if __name__ == "__main__":
    app.run(debug=True)
