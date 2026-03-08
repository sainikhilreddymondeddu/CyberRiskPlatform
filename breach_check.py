import requests

def check_email_breach(email):

    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {
                "breached": False,
                "source": "None",
                "year": "N/A",
                "data": "N/A",
                "count": 0
            }

        data = response.json()

        breaches = data.get("breaches", [])

        if breaches and len(breaches[0]) > 0:

            breach_names = breaches[0]

            return {
                "breached": True,
                "source": breach_names[0],
                "year": "Unknown",
                "data": "Multiple breach datasets",
                "count": len(breach_names)
            }

        return {
            "breached": False,
            "source": "None",
            "year": "N/A",
            "data": "N/A",
            "count": 0
        }

    except Exception as e:

        print("Breach API error:", e)

        return {
            "breached": False,
            "source": "None",
            "year": "N/A",
            "data": "N/A",
            "count": 0
        }