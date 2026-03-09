def calculate_risk(ports, breach_found, phishing_result):

    # -----------------------
    # NETWORK RISK (max 50)
    # -----------------------

    network_score = 0

    port_weights = {
        445: 10,   # SMB
        3389: 10,  # RDP
        135: 8,    # RPC
        139: 8,    # NetBIOS
        21: 8,     # FTP
        23: 10,    # Telnet
        80: 4,     # HTTP
        443: 2,    # HTTPS
        22: 4      # SSH
    }

    for p in ports:

        port = p["port"]

        if port in port_weights:
            network_score += port_weights[port]
        else:
            network_score += 2

    if network_score > 50:
        network_score = 50

    # -----------------------
    # HUMAN RISK (max 30)
    # -----------------------

    if phishing_result == "High Risk":
        human_score = 30

    elif phishing_result == "Medium Risk":
        human_score = 15

    else:
        human_score = 0

    # -----------------------
    # CREDENTIAL RISK (max 20)
    # -----------------------

    if breach_found:
        breach_score = 20
    else:
        breach_score = 0

    # -----------------------
    # FINAL SCORE
    # -----------------------

    total_score = network_score + human_score + breach_score

    if total_score > 100:
        total_score = 100

    return total_score