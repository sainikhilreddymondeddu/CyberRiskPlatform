from scanner import scan_target
from breach_check import check_email_breach
from phishing_test import phishing_behavior


def calculate_risk(target_ip, email, phishing_answer):

    ports = scan_target(target_ip)

    breach = check_email_breach(email)

    phishing = phishing_behavior(phishing_answer)

    risk_score = 0

    # Technical risk
    if len(ports) > 5:
        risk_score += 50
    elif len(ports) > 0:
        risk_score += 30

    # Breach exposure
    if breach:
        risk_score += 40

    # Phishing behaviour
    if phishing == "High Risk":
        risk_score += 30

    return ports, breach, phishing, risk_score