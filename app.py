from flask import Flask, render_template, request, send_file
import socket
import time
import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from scanner import scan_target
from breach_check import check_email_breach
from phishing_test import phishing_behavior
from risk_engine import calculate_risk

from database import init_db, save_scan, get_history, get_report

app = Flask(__name__)

latest_result = None

# Initialize database
init_db()


def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return "127.0.0.1"


def get_threat_level(score):

    if score <= 30:
        return "LOW"

    elif score <= 60:
        return "MEDIUM"

    elif score <= 80:
        return "HIGH"

    else:
        return "CRITICAL"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/scanner", methods=["GET", "POST"])
def scanner():

    global latest_result

    if request.method == "POST":

        target_ip = request.form["ip"]
        email = request.form["email"]
        phishing_choice = request.form["phishing"]

        start_time = time.time()

        ports = scan_target(target_ip)

        breach_info = check_email_breach(email)

        phishing = phishing_behavior(phishing_choice)

        score = calculate_risk(ports, breach_info["breached"], phishing)

        end_time = time.time()

        scan_time = round(end_time - start_time, 2)

        threat_level = get_threat_level(score)

        result = {
            "score": score,
            "breach": breach_info,
            "phishing": phishing,
            "ports": ports,
            "target": target_ip,
            "port_count": len(ports),
            "scan_time": scan_time,
            "threat_level": threat_level
        }

        latest_result = result

        save_scan(result)

        return render_template("report.html", result=result)

    return render_template("scanner.html", ip=get_local_ip())


@app.route("/history")
def history():

    history_data = get_history()

    return render_template("history.html", history=history_data)


# Download report for latest scan
@app.route("/download_report")
def download_report():

    global latest_result

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, y, "Cyber Security Scan Report")

    y -= 40

    p.setFont("Helvetica", 12)

    p.drawString(50, y, f"Target: {latest_result['target']}")
    y -= 20

    p.drawString(50, y, f"Risk Score: {latest_result['score']}")
    y -= 20

    p.drawString(50, y, f"Threat Level: {latest_result['threat_level']}")
    y -= 20

    breach = latest_result["breach"]

    p.drawString(50, y, f"Email Breach: {breach['breached']}")
    y -= 20

    p.drawString(50, y, f"Breach Source: {breach['source']}")
    y -= 20

    p.drawString(50, y, f"Breaches Found: {breach['count']}")
    y -= 20

    p.drawString(50, y, f"Exposed Data: {breach['data']}")
    y -= 20

    p.drawString(50, y, f"Phishing Behaviour: {latest_result['phishing']}")
    y -= 20

    p.drawString(50, y, f"Scan Duration: {latest_result['scan_time']} seconds")

    y -= 40

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y, "Detected Ports")

    y -= 20

    p.setFont("Helvetica", 10)

    for port in latest_result["ports"]:

        text = f"Port {port['port']} - {port['service']} | Severity: {port['severity']}"
        p.drawString(50, y, text)

        y -= 15

        if y < 50:
            p.showPage()
            y = 750

    p.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="cyber_security_report.pdf",
        mimetype="application/pdf"
    )


# Download report from scan history
@app.route("/download-report/<int:scan_id>")
def download_history_report(scan_id):

    result = get_report(scan_id)

    if not result:
        return "Report not found"

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, y, "Cyber Security Scan Report")

    y -= 40

    p.setFont("Helvetica", 12)

    p.drawString(50, y, f"Target: {result['target']}")
    y -= 20

    p.drawString(50, y, f"Risk Score: {result['score']}")
    y -= 20

    p.drawString(50, y, f"Threat Level: {result['threat_level']}")
    y -= 20

    breach = result["breach"]

    p.drawString(50, y, f"Email Breach: {breach['breached']}")
    y -= 20

    p.drawString(50, y, f"Breach Source: {breach['source']}")
    y -= 20

    p.drawString(50, y, f"Breaches Found: {breach['count']}")
    y -= 20

    p.drawString(50, y, f"Exposed Data: {breach['data']}")
    y -= 20

    p.drawString(50, y, f"Phishing Behaviour: {result['phishing']}")
    y -= 20

    p.drawString(50, y, f"Total Open Ports: {result['port_count']}")

    y -= 40

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y, "Detected Ports")

    y -= 20

    p.setFont("Helvetica", 10)

    for port in result["ports"]:

        text = f"Port {port['port']} - {port['service']} | Severity: {port['severity']}"
        p.drawString(50, y, text)

        y -= 15

        if y < 50:
            p.showPage()
            y = 750

    p.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"scan_{scan_id}_report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)