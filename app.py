from flask import Flask, render_template, request
import socket

from scanner import scan_target
from breach_check import check_email_breach
from phishing_test import phishing_behavior
from risk_engine import calculate_risk

app = Flask(__name__)


def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "127.0.0.1"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/scanner", methods=["GET", "POST"])
def scanner():

    if request.method == "POST":

        target_ip = request.form["ip"]
        email = request.form["email"]
        phishing_choice = request.form["phishing"]

        # Run scan
        ports = scan_target(target_ip)

        # Check breach
        breach = check_email_breach(email)

        # Phishing behavior
        phishing = phishing_behavior(phishing_choice)

        # Calculate score
        score = calculate_risk(ports, breach, phishing)

        result = {
            "score": score,
            "breach": breach,
            "phishing": phishing,
            "ports": ports,
            "target": target_ip,
            "port_count": len(ports)
        }

        return render_template("report.html", result=result)

    return render_template("scanner.html", ip=get_local_ip())


if __name__ == "__main__":
    app.run(debug=True)