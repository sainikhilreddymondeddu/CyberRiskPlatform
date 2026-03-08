def calculate_risk(ports, breach, phishing):

    score = 0

    score += len(ports) * 10

    if breach:
        score += 30

    if phishing == "High Risk":
        score += 30

    if score > 100:
        score = 100

    return score