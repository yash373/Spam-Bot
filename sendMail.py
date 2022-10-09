import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(fromEmail, toEmail, subject, message, times):
    server = smtplib.SMTP('smtp.sendgrid.net', 25)
    server.starttls()
    server.ehlo()
    server.login(
        "apikey", "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")
    for i in range(times):
        msg = MIMEMultipart()
        msg.set_unixfrom("Credits")
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = f"{subject} ({i+1}/{times})"
        msg.attach(MIMEText(message))
        server.sendmail(fromEmail, toEmail, msg.as_string())
        print(f"Sent Mail ({i+1}/{times}) to {toEmail}")
    server.quit()
