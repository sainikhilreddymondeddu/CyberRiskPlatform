from flask import Flask, render_template, request
from risk_engine import calculate_risk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        ip = request.form["ip"]
        email = request.form["email"]
        phishing = request.form["phishing"]

        ports, breach, phishing_result, score = calculate_risk(ip, email, phishing)

        result = {
            "ports": ports,
            "breach": breach,
            "phishing": phishing_result,
            "score": score
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)