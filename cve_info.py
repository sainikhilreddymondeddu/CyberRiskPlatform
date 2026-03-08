# cve_info.py

CVE_DATABASE = {

    "HTTP": [
        {
            "cve": "CVE-2021-41773",
            "description": "Apache path traversal vulnerability allowing file disclosure."
        },
        {
            "cve": "CVE-2017-5638",
            "description": "Apache Struts remote code execution vulnerability."
        }
    ],

    "MSRPC": [
        {
            "cve": "CVE-2022-26809",
            "description": "Windows RPC remote code execution vulnerability."
        }
    ],

    "NETBIOS-SSN": [
        {
            "cve": "CVE-2008-4250",
            "description": "Microsoft NetBIOS vulnerability used by Conficker worm."
        }
    ],

    "MICROSOFT-DS": [
        {
            "cve": "CVE-2017-0144",
            "description": "SMB vulnerability exploited by WannaCry ransomware."
        },
        {
            "cve": "CVE-2020-0796",
            "description": "SMBGhost vulnerability allowing remote code execution."
        }
    ],

    "SSH": [
        {
            "cve": "CVE-2018-15473",
            "description": "OpenSSH user enumeration vulnerability."
        }
    ],

    "FTP": [
        {
            "cve": "CVE-2015-3306",
            "description": "ProFTPD remote code execution vulnerability."
        }
    ]

}


def get_cve_info(service):

    service = service.upper()

    if service in CVE_DATABASE:
        return CVE_DATABASE[service]

    return []