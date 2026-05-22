import config
from smtplib import SMTP
from email.message import EmailMessage

def send(old_data, new_data):
    print("Connect to SMTP server")
    s = SMTP(config.SMTP_SERVER)
    s.starttls()
    s.login(config.SMTP_LOGIN, config.SMTP_PASSWORD)
    print("Send email")
    msg = EmailMessage()
    msg['Subject'] = config.MAIL_SUBJECT
    msg['From'] = config.MAIL_FROM
    msg['To'] = config.MAIL_TO
    msg.set_content(f"Data changed from \"{old_data}\" to \"{new_data}\"")
    s.send_message(msg)
    print("Email sent")


def check_and_notify(new_data, old_data) -> bool:
    if new_data == old_data:
        print("No changes")
        return False

    print(f"Data changed from {old_data} to {new_data}")

    send(old_data, new_data)
    return True
