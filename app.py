from flask import Flask,render_template,request
from model import predict_email

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():

    prediction=""

    if request.method=="POST":

        email=request.form["email"]

        prediction=predict_email(email)

        if prediction=="phishing":
            prediction="⚠️ Phishing Email"

        else:
            prediction="✅ Safe Email"

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__=="__main__":
    app.run(debug=True)
