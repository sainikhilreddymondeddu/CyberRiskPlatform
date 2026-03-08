# port_info.py

PORT_INTELLIGENCE = {

    21: {
        "service": "FTP",
        "category": "File Transfer Service",
        "risk": "FTP may allow attackers to access or upload files if anonymous login or weak credentials are enabled.",
        "attacks": [
            "Anonymous Login Abuse",
            "Credential Brute Force",
            "FTP Bounce Attack"
        ],
        "recommendation": [
            "Disable anonymous FTP login",
            "Use SFTP instead of FTP",
            "Restrict FTP access via firewall"
        ],
        "severity": "medium"
    },

    22: {
        "service": "SSH",
        "category": "Remote Access Service",
        "risk": "SSH brute-force attacks may allow attackers to gain remote shell access.",
        "attacks": [
            "Brute Force Login",
            "Credential Stuffing",
            "Key Theft Attacks"
        ],
        "recommendation": [
            "Disable password login and use SSH keys",
            "Change default SSH port",
            "Enable fail2ban or brute-force protection"
        ],
        "severity": "medium"
    },

    23: {
        "service": "Telnet",
        "category": "Remote Access Service",
        "risk": "Telnet transmits credentials without encryption and attackers can intercept them.",
        "attacks": [
            "Credential Sniffing",
            "Session Hijacking"
        ],
        "recommendation": [
            "Disable Telnet completely",
            "Replace Telnet with SSH",
            "Block port 23 on firewall"
        ],
        "severity": "high"
    },

    25: {
        "service": "SMTP",
        "category": "Email Service",
        "risk": "Mail servers may allow spam relays or email spoofing if misconfigured.",
        "attacks": [
            "Spam Relay Abuse",
            "Email Spoofing",
            "Phishing Infrastructure"
        ],
        "recommendation": [
            "Disable open mail relay",
            "Enable SPF, DKIM and DMARC",
            "Restrict SMTP access externally"
        ],
        "severity": "medium"
    },

    53: {
        "service": "DNS",
        "category": "Domain Name Service",
        "risk": "DNS services may allow cache poisoning or amplification attacks.",
        "attacks": [
            "DNS Cache Poisoning",
            "DNS Amplification DDoS"
        ],
        "recommendation": [
            "Disable recursive queries for external users",
            "Implement DNSSEC",
            "Rate limit DNS queries"
        ],
        "severity": "medium"
    },

    80: {
        "service": "HTTP",
        "category": "Web Service",
        "risk": "Web servers may expose vulnerabilities like XSS, directory traversal, or outdated CMS exploits.",
        "attacks": [
            "Cross-Site Scripting (XSS)",
            "SQL Injection",
            "Directory Traversal"
        ],
        "recommendation": [
            "Keep web server software updated",
            "Deploy Web Application Firewall (WAF)",
            "Disable unnecessary directories and modules"
        ],
        "severity": "medium"
    },

    135: {
        "service": "RPC",
        "category": "Windows Service",
        "risk": "RPC services may expose Windows system services to remote exploitation.",
        "attacks": [
            "Remote Service Exploitation",
            "Privilege Escalation"
        ],
        "recommendation": [
            "Restrict RPC access via firewall",
            "Disable unused Windows services",
            "Keep system fully patched"
        ],
        "severity": "high"
    },

    139: {
        "service": "NetBIOS",
        "category": "Windows Networking",
        "risk": "NetBIOS sessions may expose shared resources and allow enumeration.",
        "attacks": [
            "Network Enumeration",
            "SMB Relay Attacks"
        ],
        "recommendation": [
            "Disable NetBIOS if not required",
            "Block ports 137-139 on external networks",
            "Restrict file sharing permissions"
        ],
        "severity": "high"
    },

    443: {
        "service": "HTTPS",
        "category": "Secure Web Service",
        "risk": "HTTPS services may still be vulnerable due to weak TLS configuration or vulnerable applications.",
        "attacks": [
            "TLS Downgrade Attacks",
            "Certificate Spoofing"
        ],
        "recommendation": [
            "Use modern TLS versions (TLS 1.2+)",
            "Disable weak ciphers",
            "Renew and verify SSL certificates"
        ],
        "severity": "medium"
    },

    445: {
        "service": "SMB",
        "category": "Windows File Sharing",
        "risk": "SMB vulnerabilities like EternalBlue may allow ransomware attacks.",
        "attacks": [
            "EternalBlue (WannaCry)",
            "SMB Relay",
            "NTLM Hash Theft"
        ],
        "recommendation": [
            "Disable SMBv1",
            "Block port 445 externally",
            "Apply latest Windows security patches"
        ],
        "severity": "critical"
    },

    3389: {
        "service": "RDP",
        "category": "Remote Desktop Service",
        "risk": "RDP services may allow brute-force login attacks.",
        "attacks": [
            "Brute Force Login",
            "BlueKeep Exploit"
        ],
        "recommendation": [
            "Enable Network Level Authentication",
            "Restrict RDP access via VPN",
            "Use strong passwords and MFA"
        ],
        "severity": "high"
    }

}


def get_port_info(port, service_name=None):

    if port in PORT_INTELLIGENCE:
        info = PORT_INTELLIGENCE[port]

    else:
        info = {
            "service": service_name if service_name else "Unknown Service",
            "category": "Unknown Service",
            "risk": "Unknown service exposed. Open ports increase attack surface.",
            "attacks": [
                "Service Enumeration",
                "Exploit Probing"
            ],
            "recommendation": [
                "Close the port if unnecessary",
                "Restrict access via firewall",
                "Monitor service logs"
            ],
            "severity": "low"
        }

    return info