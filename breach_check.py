import requests

def check_email_breach(email):

    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"

    headers = {
        "User-Agent": "CyberRiskScanner"
    }

    try:

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            data = response.json()

            if data["Breaches"]:
                return True

        return False

    except:
        return False