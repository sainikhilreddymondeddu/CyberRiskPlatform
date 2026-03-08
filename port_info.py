# port_info.py

COMMON_PORTS = {

21: ("FTP", "FTP may allow attackers to access or upload files if anonymous login or weak credentials are enabled.", "medium"),

22: ("SSH", "SSH brute-force attacks may allow attackers to gain remote shell access.", "medium"),

23: ("Telnet", "Telnet transmits data without encryption and can expose credentials.", "high"),

25: ("SMTP", "Mail servers may allow spam relays or email spoofing if misconfigured.", "medium"),

53: ("DNS", "DNS services may allow cache poisoning or information disclosure.", "medium"),

80: ("HTTP", "Web servers may expose vulnerabilities like XSS, directory traversal, or outdated software.", "medium"),

110: ("POP3", "POP3 mail services may expose credentials if not secured.", "medium"),

135: ("RPC", "RPC service may expose Windows services that attackers can exploit remotely.", "high"),

137: ("NetBIOS Name Service", "NetBIOS name service may leak system information.", "medium"),

139: ("NetBIOS Session", "NetBIOS session service may allow unauthorized file access.", "high"),

143: ("IMAP", "IMAP services may expose mail authentication vulnerabilities.", "medium"),

443: ("HTTPS", "HTTPS services may expose vulnerabilities if TLS or web server configuration is weak.", "medium"),

445: ("SMB", "SMB vulnerabilities like EternalBlue may allow ransomware attacks.", "critical"),

3306: ("MySQL", "Open MySQL databases may allow unauthorized database access.", "high"),

3389: ("RDP", "Remote Desktop services may allow brute-force login attacks.", "high"),

8080: ("HTTP-Alt", "Alternative web server ports may expose web applications or admin panels.", "medium"),

5900: ("VNC", "VNC remote desktop services may allow unauthorized remote control.", "high")

}


def get_port_info(port, service_name=None):

    if port in COMMON_PORTS:
        service, risk, severity = COMMON_PORTS[port]

    else:

        service = service_name if service_name else "Unknown Service"

        risk = (
            "An unknown service is exposed on this port. "
            "Open ports increase the attack surface and attackers may probe this service for vulnerabilities."
        )

        severity = "low"

    return {
        "service": service,
        "risk": risk,
        "severity": severity
    }