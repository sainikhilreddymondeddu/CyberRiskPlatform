import random


def generate_phishing_scenario():

    scenarios = [

        {
            "id": "session_expired",
            "title": "Session Expired",
            "message": "Your account session has expired. Please login again to continue.",
            "style": random.choice(["fullscreen", "popup"])
        },

        {
            "id": "security_alert",
            "title": "Security Alert",
            "message": "Unusual login attempt detected from a new device. Please verify your identity.",
            "style": random.choice(["popup", "banner"])
        },

        {
            "id": "account_verification",
            "title": "Account Verification Required",
            "message": "Your account will be suspended within 24 hours unless you verify your credentials.",
            "style": random.choice(["fullscreen", "banner"])
        },

        {
            "id": "document_share",
            "title": "Shared Document",
            "message": "You received a shared document. Please login to view the file.",
            "style": random.choice(["popup", "banner"])
        },

        {
            "id": "password_reset",
            "title": "Password Reset Required",
            "message": "Your password has expired. Reset your password immediately.",
            "style": random.choice(["fullscreen", "popup"])
        }

    ]

    return random.choice(scenarios)


def evaluate_phishing_behavior(action):

    if action == "enter_credentials":
        return "High Risk"

    elif action == "close_page":
        return "Medium Risk"

    elif action == "report_phishing":
        return "Safe Behavior"

    else:
        return "Unknown"