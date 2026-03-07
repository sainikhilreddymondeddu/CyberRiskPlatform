# Cyber Risk Intelligence Platform

## Overview
Cyber Risk Intelligence Platform is a prototype system that evaluates cybersecurity risks by combining both **technical vulnerabilities** and **human behavior factors**.

The system analyzes:
- Network vulnerabilities (using Nmap)
- Email breach exposure
- Phishing behavior

It then calculates an **overall Cyber Risk Score**.

---

## Problem Statement
Most cybersecurity tools focus only on technical vulnerabilities such as open ports or insecure services.

However, many cyber attacks also occur due to **human errors**, such as clicking phishing links or exposing credentials.

This project demonstrates a system that evaluates **both technical and human risk factors together**.

---

## Features
- Network port scanning using Nmap
- Email breach detection
- Phishing awareness test
- Cyber risk score calculation
- Web dashboard using Flask

---

## Technologies Used
- Python
- Flask
- Nmap
- HTML
- Git & GitHub

---

## How It Works
1. User enters target IP and email.
2. System scans open ports using Nmap.
3. Email is checked against breach dataset.
4. User answers a phishing scenario.
5. System calculates the Cyber Risk Score.
6. Security report is displayed.

---

## Example Output
Open Ports: [80, 135, 137, 445]  
Email Breach: True  
Phishing Behaviour: High Risk  
Cyber Risk Score: 100

---

## Author
Sai Nikhil Reddy  
RGUKT Nuzvid