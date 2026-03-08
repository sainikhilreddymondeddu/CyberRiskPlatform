# Cyber Risk Intelligence Platform

A cybersecurity analysis platform that evaluates system security risks using **network scanning, email breach detection, and phishing behavior analysis**.

The platform scans open ports using **Nmap**, checks whether an email has appeared in known **data breaches**, and simulates **phishing behavior** to generate a **Cyber Risk Score** along with a detailed security report.

---

## Overview

Modern cyberattacks occur not only due to technical vulnerabilities but also because of **human errors**, such as clicking phishing links or exposing credentials. Traditional security tools focus mainly on system vulnerabilities and often ignore human behavior.

This project combines both approaches by analyzing:

- Network vulnerabilities
- Data breach exposure
- User phishing behavior

The result is a **Cyber Risk Score** and a **detailed vulnerability report**.

---

## Features

- Network port scanning using **Nmap**
- Detection of open ports and exposed services
- Risk explanation for detected ports
- Email breach detection using public breach databases
- Phishing behavior simulation
- Cyber Risk Score calculation
- Interactive cybersecurity report dashboard

---

## Technologies Used

**Backend**
- Python
- Flask

**Security Tools**
- Nmap
- Python-Nmap

**Frontend**
- HTML
- CSS
- Bootstrap

**Other Libraries**
- Requests

---

## Project Structure

```
CyberRiskPlatform
│
├── app.py                 # Main Flask application
├── scanner.py             # Nmap scanning module
├── port_info.py           # Port risk intelligence database
├── breach_check.py        # Email breach detection
├── phishing_test.py       # Phishing behavior simulation
├── risk_engine.py         # Cyber risk score calculation
│
├── templates
│   ├── home.html          # Landing page
│   ├── scanner.html       # Scan input page
│   └── report.html        # Security report dashboard
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CyberRiskPlatform.git
cd CyberRiskPlatform
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask python-nmap requests
```

---

### 3. Install Nmap

Download and install Nmap from:

https://nmap.org/download.html

Make sure the Nmap installation directory is added to your system **PATH**.

---

## Running the Project

Start the application:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How It Works

1. The user enters:
   - Target IP address
   - Email address
   - Phishing behavior selection

2. The platform performs:
   - **Port scanning using Nmap**
   - **Email breach detection**
   - **Phishing behavior analysis**

3. The system generates:
   - Cyber Risk Score
   - Security report
   - List of detected open ports with risk explanations

---

## Example Report Output

The generated security report includes:

- Risk Score
- Email Breach Status
- Phishing Behavior Result
- Target Scanned
- Total Open Ports
- Detected Ports with Risk Explanations

Example:

```
Risk Score: 50

Email Breach: False
Phishing Behavior: Safe Behavior
Target Scanned: 10.53.36.215
Total Open Ports: 5

Detected Ports
Port 80 (HTTP)
Risk: Web servers may expose vulnerabilities like XSS or outdated software.

Port 135 (RPC)
Risk: RPC services may allow attackers to exploit Windows services remotely.
```

---

## Security Disclaimer

This tool is created for **educational and research purposes only**.

Do not scan systems without proper authorization.

---

## Version

Current Release: **v1.0**

---

## Future Improvements

Planned features for future versions:

- Risk distribution charts
- Scan history storage
- Exportable PDF security reports
- Real-time scanning animation
- Advanced vulnerability intelligence
- User authentication dashboard

---

## Author

Mondeddu Sai Nikhil Reddy  
ECE Student – RGUKT Nuzvid  
Cybersecurity Enthusiast