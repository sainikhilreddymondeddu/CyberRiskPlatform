# Cyber Risk Intelligence Platform

A web-based cybersecurity assessment tool that analyzes system exposure, detects breached accounts, and evaluates phishing awareness to generate a comprehensive cyber risk score.

Developed by **Mondeddu Sai Nikhil Reddy**

---

## Overview

The **Cyber Risk Intelligence Platform** simulates a real-world cyber risk evaluation system.  
It combines **technical vulnerability analysis** with **human behavior analysis** to measure overall cybersecurity risk.

The platform performs:

- Network port scanning
- Email breach detection
- Phishing awareness simulation
- Cyber risk scoring
- Security report generation
- Scan history tracking

This project demonstrates how organizations can combine **technical vulnerabilities and human behavior risks** to evaluate cybersecurity posture.

---

## Key Features

### Network Port Scanning
The platform scans a target system to identify open ports and exposed services. Each detected service is analyzed for potential risks and common attack vectors.

### Email Breach Detection
Checks whether a provided email address appears in known data breach datasets and reports exposure risk.

### Phishing Behavior Simulation
Simulates phishing scenarios to evaluate user awareness and security behavior.

### Cyber Risk Score
Combines multiple factors such as:

- Open ports
- Service vulnerabilities
- Email breach exposure
- Phishing behavior

to generate a unified **Cyber Risk Score**.

### Security Report Generation
After each scan, the system generates a detailed security report including:

- Risk score
- Threat level
- Breach details
- Phishing behavior result
- Open ports and service risks

Reports can also be downloaded as **PDF files**.

### Scan History
All scans are stored in a local database and displayed in a history dashboard where users can:

- Review previous scans
- Track risk levels
- Download past reports

---

## System Architecture

```
User Interface (Flask Templates)
        |
Flask Web Server
        |
Security Modules
    ├── Port Scanner
    ├── Breach Detection
    ├── Phishing Simulation
    └── Risk Engine
        |
SQLite Database (Scan History)
```

---

## Technologies Used

### Backend
- Python
- Flask

### Security Tools
- Nmap (for network scanning)

### Frontend
- HTML
- CSS
- Bootstrap

### Database
- SQLite

### Reporting
- ReportLab (PDF generation)

---

## Project Structure

```
CyberRiskPlatform/
│
├── app.py
├── scanner.py
├── breach_check.py
├── phishing_engine.py
├── risk_engine.py
├── database.py
│
├── templates/
│   ├── home.html
│   ├── scanner.html
│   ├── report.html
│   └── history.html
│
├── scan_history.db
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/CyberRiskPlatform.git
```

Navigate to the project directory

```
cd CyberRiskPlatform
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open the browser and visit

```
http://127.0.0.1:5000
```

---

## How It Works

1. User enters target IP and email.
2. The system scans the target for open ports.
3. Email breach status is checked.
4. Phishing behavior is evaluated.
5. Risk Engine calculates the Cyber Risk Score.
6. A detailed report is generated.
7. Scan results are stored in the database.

---

## Example Output

```
Target: 10.53.36.215
Risk Score: 52
Threat Level: MEDIUM
Email Breach: True
Phishing Behaviour: Safe Behavior
Scan Duration: 8 seconds
Detected Ports: 80, 135, 139, 445
```

---

## Educational Purpose

This project is intended for **educational and research purposes only**.

Only scan systems that you **own or have permission to test**.

---

## Future Improvements

Possible enhancements include:

- Automatic network discovery
- Real-time vulnerability database integration
- Risk visualization dashboards
- Machine learning based risk prediction
- Advanced phishing scenario simulation

---

## Author

**Mondeddu Sai Nikhil Reddy**  
RGUKT Nuzvid