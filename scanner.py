import subprocess
import xml.etree.ElementTree as ET

from port_info import get_port_info
from cve_info import get_cve_info


def scan_target(target):

    ports = []

    try:

        command = [
            "nmap",
            "-sS",
            "-sV",
            "-T4",
            "--top-ports",
            "1000",
            "-oX",
            "-",
            target
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        xml_output = result.stdout
        root = ET.fromstring(xml_output)

        for port in root.findall(".//port"):

            port_id = int(port.attrib["portid"])

            state = port.find("state").attrib["state"]

            if state != "open":
                continue

            service = port.find("service")

            service_name = service.attrib.get("name", "unknown")
            product = service.attrib.get("product", "")
            version = service.attrib.get("version", "")

            server = ""

            if product or version:
                server = f"{product} {version}".strip()

            info = get_port_info(port_id, service_name)

            cves = get_cve_info(service_name)

            ports.append({
                "port": port_id,
                "service": service_name.upper(),
                "server": server,
                "category": info["category"],
                "risk": info["risk"],
                "attacks": info["attacks"],
                "recommendation": info["recommendation"],
                "severity": info["severity"],
                "cves": cves
            })

    except Exception as e:

        print("Scan error:", e)

    return ports