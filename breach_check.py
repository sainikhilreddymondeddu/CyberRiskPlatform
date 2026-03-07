def check_email_breach(email):

    breached_emails = [
        "admin@gmail.com",
        "test@example.com",
        "user@yahoo.com"
    ]

    if email in breached_emails:
        return True
    else:
        return False


if __name__ == "__main__":

    email = input("Enter email to check: ")

    if check_email_breach(email):
        print("WARNING: Email found in breach database!")
    else:
        print("Email not found in breach database.")