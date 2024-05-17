import os
import smtplib
import ssl


def send_email(message):
    user = "mahdimeyghani02@gmail.com"
    password = os.getenv("NewsAPIs")

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    receiver = "mahdimeyghani02@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)
