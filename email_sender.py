import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send_email(self):
        #add your email here
        sender = ""
        #add your password
        passwd = ""
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = sender
        message["To"] = self.recipient
        text = """{}""".format(self.body)
        plain_text = MIMEText(text, "plain")
        message.attach(plain_text)
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(sender, passwd)
        # sending the mail
        s.sendmail(sender, self.recipient, message.as_string())
        # terminating the session
        s.quit()
        print("Email sent")

subject = input("Subject\t\t")
body = input("Body\t\t")
recipient = input("Recipient\t\t")

obj = Email(recipient, subject, body)
s = obj.send_email()
